def is_anagram(test, original):
    lowerWord1 = test.lower()
    lowerWord2 = original.lower()
    if sorted(lowerWord1) == sorted(lowerWord2):
        return True
    else:
        return False