import collections
Nucleotides = ['A','T','C','G']

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
