def count(given_string):
    NewDict = {}
    if given_string == '':
        return {}
    else:
        for let in given_string:
            countlet = given_string.count(let)
            makeDict = {let:countlet}
            NewDict.update(makeDict)
    return NewDict