def count_sheep(num):
    result = ""
    for n in range(1,num+1):
        sheep = f'{n} sheep...'
        result += sheep
    return result