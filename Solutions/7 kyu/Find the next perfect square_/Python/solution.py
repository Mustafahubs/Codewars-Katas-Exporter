def find_next_square(sq):
    if int(sq ** 0.5) ** 2 != sq:
        return -1
    root = int(sq ** 0.5) + 1
    return root ** 2
