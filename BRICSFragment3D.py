#Filters:
#BRICS -> Including Non Leaf -> Only Terminal Fragments -> IGNORING Chemical Env
#-> MW Limit of 130 g/mol

import rdkit
import sys
from rdkit import Chem
from rdkit.Chem import BRICS
from rdkit.Chem import AllChem
from rdkit.Chem.rdMolAlign import AlignMol
from rdkit.Chem.Descriptors import MolWt
from rdkit.Chem.rdmolfiles import MolFromPDBFile
from rdkit.Chem.rdmolfiles import PDBWriter
from rdkit.Chem import Draw,PyMol,rdFMCS
from rdkit import rdBase

# input - .pdb file of ligand
# output - set of .pdb file pairs with corresponding pseudo-ligand and fragment
# MAKE SURE 3D OUTPUT IS ALIGNED WITH ORIGINAL FILE

def alignMolecules(substruct, fullMol): # First arg needs to be a smiles string, second needs to be a mol
    # Return Set = frag, pseudo
    patt = Chem.MolFromSmarts(substruct)
    #fragment = Chem.MolFromSmiles(substruct) # Convert .smi to mol format
    #Chem.SanitizeMol(fragment)
    #AllChem.EmbedMolecule(fragment)
    #AlignMol(fragment,fullMol)

    pseudo = AllChem.DeleteSubstructs(fullMol,patt)
    fragment = AllChem.DeleteSubstructs(fullMol,pseudo)
    # Return aligned 3D Fragment and Pseudo
    return [pseudo, fragment]


if(len(sys.argv) != 2):
    print("Need input file (.pdb format)")
    sys.exit()
try:
    mol = MolFromPDBFile(sys.argv[1])
except Exception as e:
    sys.exit()
try:
    pieces = BRICS.BRICSDecompose(mol,keepNonLeafNodes=True)                    # Printing To Confirm Proper Functionality
    count = 1
    for piece in pieces:
        try:
            piece = piece.strip()
            if(piece.count('*') == 1):
                piece = piece.replace(piece[piece.find("["):piece.find("]")+1],"")
                MW = MolWt(Chem.MolFromSmiles(piece))
                if(MW < 200):
                    [pseudo, fragment] = alignMolecules(piece,mol)
                    if(MolWt(mol) - (MolWt(pseudo) + MolWt(fragment)) < 10):
                        # Output Fragment
                        fragFile = Chem.PDBWriter(sys.argv[1].replace(".pdb","") + "_frag" + str(count) + ".pdb")
                        fragFile.write(fragment)
                        fragFile.close()

                        # Output Pseudo-Ligand
                        pseudoFile = Chem.PDBWriter(sys.argv[1].replace(".pdb","") + "_pseudo" + str(count) + ".pdb")
                        pseudoFile.write(pseudo)
                        pseudoFile.close()

                        count = count + 1
        except Exception as e:
                print(e)
                pass
except Exception as e:
    print(e)
    pass
