from string import maketrans


def to_rna(dna_strand):
    intab = 'GCTA'
    outtab = 'CGAU'
    transtab = maketrans(intab, outtab)
    return dna_strand.translate(transtab)