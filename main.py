from DNAToolkit import *
import random

rndDNAstr = ''.join([random.choice(Nucleotides) for nuc in range(10)])

DNAstr = validateSeq(rndDNAstr)

print(countNuc(DNAstr))

