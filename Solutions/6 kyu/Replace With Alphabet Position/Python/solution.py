def alphabet_position(text):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    textLower = text.lower()
    result = []
    newResult = ''
    for let in textLower:
        if let.isalpha():
            if let in abc:
                result.append(str(abc.index(let) + 1))
                newResult = ' '.join(result)
    return str(newResult)