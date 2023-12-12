def filter_list(mixlist):
    NewList = []
    for n in mixlist:
        if type(n) == int:
            NewList.append(n)
    return NewList