import pymol
from pymol import cmd
import csv
import os

contact_colors = {
    'HY': 'red',
    'HB': 'blue',
    'AT': 'green',
    'RE': 'orange', 
    'SB': 'pink',
    'DS': 'purple'
}

def generate_gray_shades(n):
    shades = []
    for i in range(n):
        value = int(255 * (i / max(1, n - 1)))
        rgb = [value / 255.0] * 3
        color_name = f"gray_custom_{i}"
        cmd.set_color(color_name, rgb)
        shades.append(color_name)
    return shades


def load_contacts(protein_input, csv_file):
    cmd.reinitialize()
    protein_id, type = os.path.splitext(os.path.basename(protein_input))
    if type == ".cif" or type == ".pdb":
        cmd.load(protein_input, protein_id)
    else:
        cmd.fetch(protein_input, protein_id, type="cif")

    cmd.show("cartoon", protein_id)
    cmd.bg_color("white")
    
    interactions = {key: [] for key in contact_colors.keys()}
    interacting_residues = {key: [] for key in contact_colors.keys()}
    
    chain_list = set()

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            chain1, res1, resname1, atom1, chain2, res2, resname2, atom2, distance, interaction_type = row
            if interaction_type not in contact_colors:
                continue
            
            chain_list.add(chain1)
            chain_list.add(chain2)

            atom_selection1 = f"(polymer.protein and chain {chain1} and resi {res1} and name {atom1})"
            atom_selection2 = f"(polymer.protein and chain {chain2} and resi {res2} and name {atom2})"
            resi_selection1 = f"polymer.protein and chain {chain1} and resi {res1}"
            resi_selection2 = f"polymer.protein and chain {chain2} and resi {res2}"

            if cmd.count_atoms(atom_selection1) == 0:
                print(f"Warning: No atoms found for {atom_selection1}")
                continue
            if cmd.count_atoms(atom_selection2) == 0:
                print(f"Warning: No atoms found for {atom_selection2}")
                continue

            interactions[interaction_type].append((atom_selection1, atom_selection2, float(distance)))
            interacting_residues[interaction_type].append(resi_selection1)
            interacting_residues[interaction_type].append(resi_selection2)


    chain_list = sorted(chain_list)
    gray_shades = generate_gray_shades(len(chain_list))

    chain_colors = {}
    for i, chain in enumerate(chain_list):
        chain_colors[chain] = gray_shades[i]
        cmd.color(gray_shades[i], f"polymer.protein and chain {chain}")
        
    for interaction_type, contacts in interactions.items():
        if not contacts:
            print(f"No contacts for {interaction_type}")
            continue

        print(f"Interaction {interaction_type}: {len(contacts)} contacts found")

        obj_name = f"contacts_{interaction_type}"
        cmd.distance(obj_name, "none", "none")

        for sel1, sel2, distance in contacts:
            color = contact_colors.get(interaction_type, "yellow")
            cmd.distance(obj_name, sel1, sel2)

        cmd.set("dash_color", color, obj_name)

        group_name = f"group_{interaction_type}"
        cmd.group(group_name, obj_name, "add")
        cmd.group(group_name, "close")

    for interaction_type, residues in interacting_residues.items():
        residues = list(set(residues))
        if residues:
            obj_name = f"residues_{interaction_type}"
            cmd.select("temp", " or ".join(residues))
            cmd.create(obj_name, "temp")
            cmd.delete("temp")
            cmd.show("sticks", obj_name)
            cmd.hide("cartoon", obj_name)
            cmd.util.cnc(obj_name, _self=cmd)
            cmd.group(f"group_{interaction_type}", obj_name, "add")
            cmd.disable(f"group_{interaction_type}")

    cmd.orient()
    cmd.save(f"{protein_id}_visualization.pse")
