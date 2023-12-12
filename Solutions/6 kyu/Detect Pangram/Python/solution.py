def is_pangram(Given_String):
    small__abc = 'abcdefghijklmnopqrstuvwxyz'
    Lower_str = Given_String.lower()
    for let in small__abc:
        if let.isalpha():
            if let not in Lower_str:
                return False
    else:
        return True