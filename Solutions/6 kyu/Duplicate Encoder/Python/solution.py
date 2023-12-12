def duplicate_encode(word):
    count = ''
    olddata = word
    data = olddata.lower()
    for x in data:
        if data.count(x)==1: count+='('
        else: count+=')'
    return count