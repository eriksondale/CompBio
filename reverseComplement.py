# The purpose of this script is provide the reverse complement of a
# given DNA strand (i.e. The other part of a strand that can be read)

from sys import argv as argument

"""Script requires test file containing DNA sequence"""

if(len(argument) != 2):
    print("Error in argument length; DNA sequence file needed...")
else:
    with open(argument[1],'r') as DNAfile:
        DNAseq = DNAfile.read()
        DNAseq = DNAseq.upper()
        DNAseq = DNAseq.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c')
        DNAseq = DNAseq.upper()[::-1]
        print(DNAseq)
