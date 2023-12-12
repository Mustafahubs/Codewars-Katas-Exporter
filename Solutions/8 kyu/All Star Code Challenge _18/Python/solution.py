def str_count(string, letter):
    letterCount = 0 
    for let in string:
        if let == letter:
            letterCount += 1
    return letterCount