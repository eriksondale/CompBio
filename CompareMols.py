import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols
from sys import argv as argument

# Requires two .smi files with one molecule each
# If they represent the same molecule (error possible) -> result == 1

if len(argument) != 3:
    print('Need 2 .smi files to compare...')
else:
    with open(argument[1],'r') as FileA:
        try:
            molA = Chem.MolFromSmiles(FileA.read())
            with open(argument[2],'r') as FileB:
                molB = Chem.MolFromSmiles(FileB.read())
                molAbit = FingerprintMols.FingerprintMol(molA)
                molBbit = FingerprintMols.FingerprintMol(molB)
                similarity = DataStructs.FingerprintSimilarity(molAbit, molBbit)
                print(similarity)
        except:
            print('Problem reading a .smi file')
