def multi_table(number):
    Table_str = ''
    for num in range(1,11):
        multiply = num*number
        Table = f"{num} {'*'} {number} {'='} {multiply}"
        Table_str += Table
        Table_str += '\n'
    return Table_str.strip()