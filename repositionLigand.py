"""The goal of this script is to take two 3D molecule models
and to match the position of the second one to the first one
based on a matching substructure"""

import sys
from sys import argv as arg

if(len(arg) != 3):
    print("Error: Files required: 1) .pdb of molecule 2) .pdb of molecule to be moved")
    sys.exit()
if(arg[1].endsWith(".pdb") or arg[2].endsWith(".pdb") is False):
    print("Input files must be .pdb files")
    sys.exit()
baseMolFile = open(arg[1],"r")
moveMolFile = open(arg[2],"r")
pass
