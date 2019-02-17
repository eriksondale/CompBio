#Filters:
#BRICS -> Only Terminal Fragments, IGNORING Chemical Env, MW Limit of 150 g/mol

#Imports
import sys
import rdkit
from rdkit import Chem
from rdkit.Chem import BRICS
from rdkit.Chem import AllChem
from rdkit.Chem.Descriptors import MolWt
from rdkit.Chem import rdmolops
from rdkit.Chem.rdmolfiles import MolFromPDBFile
from rdkit.Chem.rdmolfiles import PDBWriter
from rdkit.Chem import Draw,PyMol,rdFMCS
from rdkit import rdBase
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem.Draw.MolDrawing import DrawingOptions

# input - .pdb file of ligand
# output - set of .pdb file pairs with corresponding pseudo-ligand and fragment

if(len(sys.argv) != 2):
    print("Need input file (.pdb format)")
    sys.exit()
try:
    mol = MolFromPDBFile(sys.argv[1]) # Reading in Mol Obj and Cleaning Up
    Chem.SanitizeMol(mol)
except Exception as e:
    sys.exit()
try:
    # Get Bonds
    bonds = BRICS.FindBRICSBonds(mol)
    bondList = list(bonds)
    breakList = []
    for bond in bondList:
        breakList.append(bond[0]) # Parsing in actual atoms associated with bonds
    breakBonds = [mol.GetBondBetweenAtoms(x,y).GetIdx() for x,y in breakList] # Getting bond number from atom pair
    count = 1
    for bond in breakBonds: # For each bond
        try:
            fragMol = Chem.FragmentOnBonds(mol,[bond],addDummies=False) # Get Mol Frags from Breaking Bonds
            frags = rdmolops.GetMolFrags(fragMol,asMols=True)
            if(len(frags)==2): # Ensuring Terminal Fragment (1 Frag = Breaking Ring, >2 Frag = Internal Fragmentation)
                if(MolWt(frags[0]) < 150 or MolWt(frags[1]) < 150): # Ensuring Small Fragments, Adjust If Too Large
                    if(MolWt(frags[0]) < MolWt(frags[1])):
                            # Output Fragment
                            fragFile = Chem.PDBWriter(sys.argv[1].replace(".pdb","") + "_frag" + str(count) + ".pdb")
                            fragFile.write(frags[0])
                            fragFile.close()

                            # Output Pseudo-Ligand
                            pseudoFile = Chem.PDBWriter(sys.argv[1].replace(".pdb","") + "_pseudo" + str(count) + ".pdb")
                            pseudoFile.write(frags[1])
                            pseudoFile.close()
                    else:
                            # Output Fragment
                            fragFile = Chem.PDBWriter(sys.argv[1].replace(".pdb","") + "_frag" + str(count) + ".pdb")
                            fragFile.write(frags[1])
                            fragFile.close()

                            # Output Pseudo-Ligand
                            pseudoFile = Chem.PDBWriter(sys.argv[1].replace(".pdb","") + "_pseudo" + str(count) + ".pdb")
                            pseudoFile.write(frags[0])
                            pseudoFile.close()
                    count = count + 1 # Advance Filing Output Numbering by 1
        except Exception as e: # Hopefully these won't happen :-) 
                print(e)
                pass
except Exception as e:
    print(e)
    pass
