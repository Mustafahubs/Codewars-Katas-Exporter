def unique_in_order(sequence):
    store = []
    lastTime = ''
    for l in sequence:
        if l != lastTime:
            store.append(l)
            lastTime = l
    return store