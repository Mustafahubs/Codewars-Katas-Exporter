def duplicate_count(text):
    lowertxt = text.lower()
    Duplicate_count = []
    for let in lowertxt:
        if lowertxt.count(let) > 1 and let not in Duplicate_count:
            Duplicate_count.append(let)
    return len(Duplicate_count)