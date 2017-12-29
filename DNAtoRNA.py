from sys import argv as argument

if(len(argument) != 2):
    print("Invalid number of arguments. Requires: DNA sequence file.")
else:
    with open(argument[1],'r') as DNAfile:
        DNAseq = DNAfile.read( )
        DNAseq = DNAseq.replace("T", "U")
        print(DNAseq)
