def tower_builder(n_floors):
    Newlist = []
    for x in range(1,n_floors+1):
        centInt = (n_floors-1) + n_floors
        stars = (x-1)*'*' +  x*'*'
        item = stars.center(centInt)
        Newlist.append(item)
    return Newlist