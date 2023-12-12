def is_isogram(string):
    string2 = ''
    Words = string.lower()
    for l in Words:
        if l in string2:
            return False
        else:
            string2 += l
    return True