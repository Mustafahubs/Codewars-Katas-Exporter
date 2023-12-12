def dna_to_rna(dna):
    RNA_Conv = ''
    for  nucleicacid in dna:
        if nucleicacid == 'G':
            RNA_Conv += 'G'
        elif nucleicacid == 'C':
            RNA_Conv += 'C'
        elif nucleicacid == 'A':
            RNA_Conv += 'A'
        elif nucleicacid == 'T':
            RNA_Conv += 'U'
    return RNA_Conv