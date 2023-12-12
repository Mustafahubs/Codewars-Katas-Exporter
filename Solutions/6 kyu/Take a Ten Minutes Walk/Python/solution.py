def is_valid_walk(walk):
    if len(walk) != 10: return False
    x = 0
    y = 0
    for dire in walk:
        if dire == 'n':
            y += 1
        elif dire == 's':
            y -= 1
        elif dire == 'e':
            x += 1
        else:
            x -= 1
    if x == 0 and y == 0: return True
    else: return False