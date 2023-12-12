def name_shuffler(String):
    Splited = String.split()
    reverse  = Splited[::-1]
    Joined_Str = ' '.join(reverse)
    return Joined_Str