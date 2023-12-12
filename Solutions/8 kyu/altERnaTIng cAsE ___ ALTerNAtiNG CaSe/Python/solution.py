def to_alternating_case(string):
    newstring = ''
    for let in string:
        if let.islower():
            newstring += let.upper()
        else:
            newstring += let.lower()
    return newstring