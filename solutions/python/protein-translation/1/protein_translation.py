def string_to_gene(strand):
    gene = []
    for i in range(0, len(strand), 3):
        if i + 2 > len(strand):
            gene.append(strand)
        codon = strand[i: i + 3]
        gene.append(codon)
    return gene


def proteins(strand):
    gene = string_to_gene(strand)
    protein_list = []
    for key_codon in gene:
        print(f"Checking {key_codon}")
        for codons, protein in PROTEIN_TO_CODON_MAP.items():
            if key_codon in codons:
                if protein == "STOP":
                    return protein_list
                protein_list.append(protein)

    return protein_list


PROTEIN_TO_CODON_MAP = {
    ("AUG"): "Methionine",
    ("UUU", "UUC"): "Phenylalanine",
    ("UUA", "UUG"): "Leucine",
    ("UCU", "UCC", "UCA", "UCG"): "Serine",
    ("UAU", "UAC"): "Tyrosine",
    ("UGU", "UGC"): "Cysteine",
    ("UGG"): "Tryptophan",
    ("UAA", "UAG", "UGA"): "STOP",
}

strand  = "UGGUGUUAUUAAUGGUUU"
print(proteins(strand))
expected = ['Tryptophan', 'Cysteine', 'Tyrosine']
