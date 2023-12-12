def invert(lst):
    Change_List = []
    for n in lst:
        if n >= 0:
            positive = n*-1
            Change_List.append(positive)
        elif n <= 0:
            negetive = n*-1
            Change_List.append(negetive)
        else:
            if lst == []:
                return [0]
    return Change_List