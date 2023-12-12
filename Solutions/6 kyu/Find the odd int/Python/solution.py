def find_it(given_list):
    for n in set(given_list):
        if given_list.count(n)%2 != 0:
            return (n) 
    return Num_list