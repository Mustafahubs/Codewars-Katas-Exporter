def descending_order(num):
    String_From = str(num)
    Number_Sorted = sorted(String_From)
    Descending_Order = Number_Sorted[::-1]
    Convert_Int = ''.join(Descending_Order)
    return int(Convert_Int)