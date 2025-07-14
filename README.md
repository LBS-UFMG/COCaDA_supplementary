<p align="center">
  <img src="https://github.com/user-attachments/assets/57f17d48-baf4-4bed-97ab-6b817e31dc26" alt="COCaDA_logomenor">
</p>

# 🧾 Supplementary files for COCαDA
---

This repository contains supplementary materials for the paper  **_"COCαDA - A Fast and Scalable Algorithm for Interatomic Contact Detection in Proteins Using Cα Distance Matrices"_**, by **Lemos *et al***.

For the main tool and source code, please visit the primary repository: [COCaDA](https://github.com/LBS-UFMG/COCaDA.git).

---

## 📁 Contents

- [`NS_Biopython/`](NS_Biopython/): Contains the custom implementation of the NeighborSearch (NS) approach using **Biopython**.
- [`D1_files/`](D1_files/): Contains the modified dataset derived from [Brown *et al.* (2006)](https://doi.org/10.1186/gb-2006-7-1-r8), comprising **896 entries**, and used as Dataset D1 in the study.
- [`PDB_entries.txt`](PDB_entries.txt): A text file listing all **217,454 PDB IDs** used to generate the maximum distance matrix.
- [`101M_contacts.csv`](101M_contacts.csv): A csv file containing an example output for PDB ID 101M. The columns are organized as follows: Chain 1, Residue Number 1, Residue Name 1, Atom Name 1, Chain 2, Residue Number 2, Residue Name 2, Atom Name 2, Distance, Contact Type.
- [`cocada_pymol_visualization.py`](cocada_pymol_visualization.py): A Python script to help users quickly visualize and explore results in PyMOL. How to use:
  - On PyMOL, click on 'File' and then 'Run Script...';
  - Open the `cocada_pymol_visualization.py` file;
  - Type `load_contacts("ID", "outputfile.csv")` on PyMOL's terminal, where ID is the desired protein PDB ID or file path, `and outputfile.csv` is the COCαDA output.
  - **Important:** make sure that the `outputfile` is in the same folder as the script.

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Contact
For any questions or issues, please contact:

**Rafael Pereira Lemos**  
PhD Student in Bioinformatics  
Federal University of Minas Gerais  

- 📧 Email: [rafaellemos42@gmail.com](mailto:rafaellemos42@gmail.com)  
- 🔗 GitHub: [@rplemos](https://github.com/rplemos)

---

## 🧠 Contributions and Acknowledgements
 - Prof. Raquel Cardoso de Melo Minardi, UFMG;
 - Prof. Sabrina de Azevedo Silveira, UFV;
 - Dr. Diego César Batista Mariano, UFMG;
 - All the 'Laboratory of Bioinformatics and Systems' team.
