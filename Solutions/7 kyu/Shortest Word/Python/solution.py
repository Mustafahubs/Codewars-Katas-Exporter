def find_short(data):
    splited = data.split()
    small = len(splited[0])
    for x in splited:
        text = len(x)
        if text<small:
            small = text
    return small