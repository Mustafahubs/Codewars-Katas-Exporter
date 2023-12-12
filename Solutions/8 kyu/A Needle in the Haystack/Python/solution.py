def find_needle(haystack):
    for word in range(len(haystack)):
        if haystack[word] == "needle":
            return f"found the needle at position {word}"
