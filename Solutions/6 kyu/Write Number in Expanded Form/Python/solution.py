def expanded_form(num):
    num_str = str(num)
    result = []
    for i in range(len(num_str)):
        if num_str[i] != '0':
            result.append(num_str[i] + '0' * (len(num_str) - i - 1))
    return ' + '.join(result)