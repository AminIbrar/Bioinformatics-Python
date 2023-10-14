DNA_Reverse_Compliment = {'A':'T','T':'A','G':'C','C':'G'}
def reverse_compliment(seq):
    """Swapping Adenine with Thymine and Guanine with Cytosine. Then Reversing the new String"""
    return ''.join([DNA_Reverse_Compliment[nuc] for nuc in seq])[::-1]

print(reverse_compliment("AAAACCCGGT"))
