def square_digits(num):
    str_num = str(num)
    concatenate_num = ""
    for digit in str_num:
        concatenate_num += str(int(digit) ** 2)
    return int(concatenate_num)