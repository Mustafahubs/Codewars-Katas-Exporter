def array_diff(a, b):
    items = []
    for n in a:
        if n not in b:
            items.append(n)
    return items