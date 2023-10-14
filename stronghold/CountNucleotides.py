def countNuc(seq):
    countDict = {'A':0,'T':0,'C':0,'G':0}
    for nuc in seq:
        countDict[nuc] += 1
    return countDict
  
DNAString = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
result = countNuc(DNAString)
print(' '.join([str(val) for key,val in result.items()]))