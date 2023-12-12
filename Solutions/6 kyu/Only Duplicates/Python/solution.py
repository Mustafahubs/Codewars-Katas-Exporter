def only_duplicates(input_str):
    char_count = {}
    
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    output_str = ""
    for char in input_str:
        if char_count[char] > 1:
            output_str += char
    return output_str
