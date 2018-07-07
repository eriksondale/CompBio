# This file contains operations for getting DNA
# sequence data and operating on it
import sys
from sys import argv as arg


# Returns True if str input is a valid DNA sequence, returns False otherwise
def Valid(seq):
    for char in seq:
        if char not in ['A','T','C','G']:
            return False
    return True

# This will print the nucleotide count of the sequence
def countNucleotides(seq):
    counts = {'A':0,'C':0,'G':0,'T':0}
    for char in seq:
        counts[char] += 1
    for count in counts:
        print(counts[count])

# Converts DNA sequence to RNA sequence
def toRNA(seq):
    return seq.replace("T","U")

# Returns reverse comlpement of DNA sequence
def getRevCompl(seq):
    seq = seq.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c')
    seq = seq.upper()[::-1]
    return seq

# GC Content, add the ability compare GC contents of multiple seqs
def GCContent(seqs):
    for key, DNAseq in seqs.iteritems():
        length = 0.0
        GCnum = 0.0
        for char in DNAseq:
            length += 1
            if char in ['C','G']:
                GCnum += 1.0
        print(key)
        print(GCnum / length * 100)


# int: two DNA sequences of equal length
# out: the Hamming Distance between the two sequences
def HammingDist(seqA, seqB):
    temp = 0
    if(len(seqA) != len(seqB)):
        return None
    else:
        for x in range(0, len(seqA)):
            if seqA[x] != seqB[x]:
                temp += 1
    return temp

# Finds locations of motifs in DNA seqence (brute for string pattern matching algorithm)
def findMotif(seq, motif):
    for x in range(0, len(seq)):
        #print(seq[x:x+len(motif)])
        if seq[x:x+len(motif)] == motif:
            print(x+1)


if(len(arg) < 2):
    DNAseqA = raw_input("Please enter DNA seq: ")
    DNAseqB = raw_input("Please enter DNA seq2: ")
    print(HammingDist(DNAseqA, DNAseqB))
else:
    if(arg[1].endswith(".fasta")):
        DNAseqs = { }
        fileText = open(arg[1],"r")
        tempID = 0
        tempSeq = ""
        for line in fileText:
            line = line.strip("\n")
            line = line.strip(" ")
            if line[0] is ">":
                if tempID != 0:
                    DNAseqs[tempID.strip(">")] = tempSeq
                    tempSeq = ""
                tempID = line
            else:
                tempSeq = tempSeq + line
        for key, DNAseq in DNAseqs.iteritems():
            DNAseq = DNAseq.upper()
            if not Valid(DNAseq):
                print("One or more DNA sequence not valid. Exiting...")
                sys.exit()
    else:
        DNAseqs = (open(arg[1], "r")).read()
        DNAseqs = DNAseqs.upper()
        if not Valid(DNAseqs):
            print("One or more DNA sequence not valid. Exiting...")
