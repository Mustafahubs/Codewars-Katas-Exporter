def remove(given_string):
    if given_string == '':
        return given_string
    if given_string[-1] == '!':
        return given_string[:-1]
    else:
        return given_string