def quarter_of(month):
    output = 0
    if int(month) in range(1,4):
        output += 1
    elif int(month) in range(4,7):
        output += 2
    elif int(month) in range(7,10):
        output += 3
    elif int(month) in range(10,13):
        output += 4
    return output