def xo(string):
    string = string.lower()    
    x_count = 0
    o_count = 0
    for char in string:
        if char == 'x':
            x_count += 1
        elif char == 'o':
            o_count += 1
    return x_count == o_count