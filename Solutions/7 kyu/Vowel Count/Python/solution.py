def get_count(Given_String):
    Vowels = "aeiouAEIOU"
    Number_of_Vowels = 0
    for letter in Given_String:
        if letter in Vowels:
            Number_of_Vowels += 1
    return Number_of_Vowels