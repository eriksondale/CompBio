# The purpose of this script is to generate a random
# DNA sequence of length n, n is an int argument

from sys import argv as argument
from random import *

"""Script requires int as argument"""

numToBase = {'0':'A','1':'T','2':'C','3':'G'}

if(len(argument) != 2):
    print("Error in argument length; int is required...")
else:
    DNAseq = ""
    for x in range(0, int(argument[1])):
        newBase = numToBase[str(randint(0,3))] 
        DNAseq = DNAseq + newBase
    print(DNAseq)
