from DNAToolkit import *
import random
from utilities import colored

rndDNAstr = ''.join([random.choice(Nucleotides) for nuc in range(20)])

DNAstr = validateSeq(rndDNAstr)

print(f"\nSequence: {colored(DNAstr)}\n")
print(f"Sequence Length: {len(DNAstr)}\n")
print(colored(f"Nucleotide Frequency {countNuc(DNAstr)}\n"))
print(f"DNA/RNA Transcription {transcription(DNAstr)}\n")
print(f"DNA String + Reverse Compliment:\n5' {colored(DNAstr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAstr))])}")
print(f"3' {colored(reverse_compliment(DNAstr))} 5'\n")