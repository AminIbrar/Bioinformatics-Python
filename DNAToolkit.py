import collections
from sequences import *

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNuc(seq):
    countDict = {'A':0,'T':0,'C':0,'G':0}
    for nuc in seq:
        countDict[nuc] += 1
    return countDict
    #return dict(collections.Counter(seq))

def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine with Uracil"""
    return seq.replace('T','U')

def reverse_compliment(seq):
    """Swapping Adenine with Thymine and Guanine with Cytosine. Then Reversing the new String"""
    return ''.join([DNA_Reverse_Compliment[nuc] for nuc in seq])[::-1]


def gc_content(seq):
    """GC content in a DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq)*100)


def gc_content_subset(seq, k=20):
    """ GC Content of DNA/RNA Sections"""
    res = []
    for i in range(0,len(seq)-k+1,k):
        subseq = seq[i:i+k]
        res.append(gc_content(subseq))
    return res
