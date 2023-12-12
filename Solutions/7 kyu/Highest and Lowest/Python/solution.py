def high_and_low(numbers):
    listofNum = []
    number_list = numbers.split()
    for n in number_list:
        listofNum.append(int(n))

        SmallestNum = str(min(listofNum))
        LargestNum = str(max(listofNum))
        high_to_low = f'{LargestNum} {SmallestNum}'
    return high_to_low