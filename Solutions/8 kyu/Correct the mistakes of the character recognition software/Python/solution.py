def correct(txt):
    newtxt = ''
    for lett in txt:
        if lett == '5':
            newtxt += 'S'
        elif lett == '0':
            newtxt += 'O'
        elif lett == '1':
            newtxt += 'I'
        else:
            newtxt += lett
    return newtxt