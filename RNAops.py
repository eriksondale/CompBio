# Try to develop to work w/ dictionaries of sequences are default one by entering

# This file contains operations for getting RNA
# sequence data and operating on it
import sys
from sys import argv as arg

# Returns True if str input is a valid DNA sequence, returns False otherwise
def Valid(seq):
    for char in seq:
        if char not in ['A','U','C','G']:
            print("error: " + char)
            return False
    return True

# Translation

def translate(RNAseq):
    codonTable = {  "UUU":"F", "UCU":"S", "UAU":"Y", "UGU":"C",
                    "UUC":"F", "UCC":"S", "UAC":"Y", "UGC":"C",
                    "UUA":"L", "UCA":"S", "UAA":"\n", "UGA":"\n",
                    "UUG":"L", "UCG":"S", "UAG":"\n", "UGG":"W",

                    "CUU":"L", "CCU":"P", "CAU":"H", "CGU":"R",
                    "CUC":"L", "CCC":"P", "CAC":"H", "CGC":"R",
                    "CUA":"L", "CCA":"P", "CAA":"Q", "CGA":"R",
                    "CUG":"L", "CCG":"P", "CAG":"Q", "CGG":"R",

                    "AUU":"I","ACU":"T", "AAU":"N", "AGU":"S",
                    "AUC":"I","ACC":"T", "AAC":"N", "AGC":"S",
                    "AUA":"I","ACA":"T", "AAA":"K", "AGA":"R",
                    "AUG":"M","ACG":"T", "AAG":"K", "AGG":"R",

                    "GUU":"V", "GCU":"A", "GAU":"D", "GGU":"G",
                    "GUC":"V", "GCC":"A", "GAC":"D", "GGC":"G",
                    "GUA":"V", "GCA":"A", "GAA":"E", "GGA":"G",
                    "GUG":"V", "GCG":"A", "GAG":"E", "GGG":"G" }

    startCodonPos = RNAseq.find('AUG')
    newSeq = RNAseq[startCodonPos:]
    proteinSeq = ''
    for nuc in range(0, len(newSeq), 3):
        if newSeq[nuc:nuc+3] in codonTable:
                if (codonTable[newSeq[nuc:nuc+3]] == '\n'):
                    return proteinSeq
                proteinSeq = proteinSeq + codonTable[newSeq[nuc:nuc+3]]

    return proteinSeq


# Main

if(len(arg) < 2):
    RNAseq = raw_input("Please enter RNA seq: ")
else:
    if(arg[1].endswith(".fasta")):
        RNAseqs = { }
        fileText = open(arg[1],"r")
        tempID = 0
        tempSeq = ""
        for line in fileText:
            line = line.strip("\n")
            line = line.strip(" ")
            if line[0] is ">":
                if tempID != 0:
                    RNAseqs[tempID.strip(">")] = tempSeq
                    tempSeq = ""
                tempID = line
            else:
                tempSeq = tempSeq + line
        for key, RNAseq in RNAseqs.iteritems():
            RNAseq = RNAseq.upper()
            if not Valid(RNAseq):
                print("One or more RNA sequence not valid. Exiting...")
                sys.exit()
    else:
        RNAseq = (open(arg[1], "r")).read()
RNAseq = RNAseq.upper()
RNAseq = RNAseq.strip("\n")
if not Valid(RNAseq):
    print("One or more RNA sequence not valid. Exiting...")
    sys.exit()
print(translate(RNAseq))
