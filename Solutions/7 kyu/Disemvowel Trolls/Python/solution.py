def disemvowel(string_):
    Vowels = 'aeiouAEIOU'
    for let in string_:
        if let in Vowels:
            string_ = string_.replace(let,'')
    return string_