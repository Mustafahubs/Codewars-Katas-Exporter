def count_smileys(arr):
    eye = ':;'
    nose = '-~'
    mouth = ')D'
    countSmiles = 0
    for smil in arr:
        if len(smil) == 2:
            if smil[0] in eye and smil[1] in mouth:
                countSmiles += 1
        else:
            if smil[0] in eye and smil[1] in nose and smil[2] in mouth:
                countSmiles += 1
    return countSmiles