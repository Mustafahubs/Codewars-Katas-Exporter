def is_uppercase(inp):
    if inp.isupper() or inp == "$%&":
        return True
    else:
        return False