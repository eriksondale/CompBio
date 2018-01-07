from sys import argv as argument
import sys

if (len(argument) != 3):
    print('Invalid number of arguments. Script requires 1) motif and 2) sequence.')
    sys.exit()
with open(argument[1], 'r') as motifFile, open(argument[2],'r') as seqFile:
    pos = ""
    motif = motifFile.read()
    seq = seqFile.read()
    for x in range(0, len(seq) - len(motif)):
        if motif == seq[x:x+len(motif)]:
            pos = pos + str(x + 1) + ' '  # Because DNA counting starts at 1...
    print(pos)
