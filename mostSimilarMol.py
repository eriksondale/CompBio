# Input: .smi of Molecule A, .smi of a list of molecules
# Output: .smi of Molecule in list that is most similar to Molecule A (based on  Tanimoto similarity)

import sys
from sys import argv as arg
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit import rdBase

if(len(arg) != 3):
    print("Need .smi of molecule and .smi of list of molecules")
else:
    with open(arg[1],"r") as mainMolFile:
        mainMolStr = mainMolFile.read()
        try:
            mainMol = Chem.MolFromSmiles(mainMolStr)
        except:
            print("Cannot read first .smi file")
            sys.exit()
        with open(arg[2],"r") as compareMolsFile:
            try:
                molList = []
                for line in compareMolsFile:
                    molList.append(Chem.MolFromSmiles(line))
            except:
                print("Problem reading second .smi file")
                sys.exit()
            mainBit = FingerprintMols.FingerprintMol(mainMol)
            bestMol = None
            bestSim = None
            for mol in molList:
                tempBit = FingerprintMols.FingerprintMol(mol)
                similarity = DataStructs.FingerprintSimilarity(mainBit, tempBit)
                if(bestSim is None):
                    bestMol = mol
                    bestSim = similarity
                elif(bestSim < similarity):
                    bestMol = mol
                    bestSim = similarity
                else:
                    pass
            print("Molecule: " + Chem.MolToSmiles(bestMol))
            print("Similarity: " + str(bestSim))
