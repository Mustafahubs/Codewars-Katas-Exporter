def number(lines):
    newlist = []
    for ind,x in enumerate(lines,1):
        store = f"{ind}: {x}"
        newlist.append(store)
    return newlist