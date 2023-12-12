def sum_dig_pow(a, b):
    result = []
    for i in range(a, b+1):
        digits = [int(d) for d in str(i)]
        if i == sum([d**(index+1) for index, d in enumerate(digits)]):
            result.append(i)
    return result