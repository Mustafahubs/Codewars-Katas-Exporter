def count_sheeps(sheep):
    count_alive_sheep = 0
    for alive in sheep:
        if alive == True:
            count_alive_sheep += 1
    return count_alive_sheep