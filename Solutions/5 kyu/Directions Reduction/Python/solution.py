def dirReduc(arr):
    directions = {"NORTH": "SOUTH","SOUTH": "NORTH","WEST": "EAST","EAST": "WEST"}
    store = []
    for dir in arr:
        if store and directions[dir] == store[-1]:
            store.pop()
        else:
            store.append(dir)
    return store
