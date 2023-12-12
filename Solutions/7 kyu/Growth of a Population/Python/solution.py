def nb_year(present_pop, percent, aug, new_poplution):
    year = 0
    while present_pop < new_poplution:
        addsol = int(present_pop * percent/100) + aug
        present_pop = addsol + present_pop
        year = year + 1
    return year