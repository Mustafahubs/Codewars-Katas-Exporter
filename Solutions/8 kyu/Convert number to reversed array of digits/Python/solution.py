def digitize(string):
    listemp = []
    ConvertStr = str(string)
    NewString = ConvertStr[::-1]
    for n in NewString:
        listemp.append(int(n))
    return listemp