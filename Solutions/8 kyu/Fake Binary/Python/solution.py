def fake_bin(number):
    newnum = ''
    for x in number:
        if x < '5':
            newnum += '0'
        if x >= '5':
            newnum += '1'
    return newnum