def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('DNA strands have different lengths!')
    hamming = 0
    check_string = ""
    for pos, letter in enumerate(strand_a):
        if strand_b[pos] != letter:
            hamming += 1
    return hamming