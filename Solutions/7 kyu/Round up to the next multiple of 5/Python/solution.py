def round_to_next5(Given_num):
    reminder = Given_num%5
    if reminder == 0:
        return Given_num
    if reminder > 0:
        return Given_num+(5-reminder)
    else:
        return reminder - 5