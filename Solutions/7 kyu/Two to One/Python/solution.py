def longest(a1, a2):
    combined = list(a1 + a2)
    unique = []
    for char in combined:
        if char not in unique:
            unique.append(char)
    combined = sorted(unique)
    return ''.join(combined)
