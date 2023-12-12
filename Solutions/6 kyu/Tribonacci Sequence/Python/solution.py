def tribonacci(givenNumbers, stopNum):
    if stopNum >= 1:
        NewList = givenNumbers
        for Num in range(4, stopNum+1):
            lastNum = givenNumbers[-1]
            secondlast = givenNumbers[-2]
            Thirdlast = givenNumbers[-3]
            next_num = lastNum + secondlast + Thirdlast
            NewList.append(next_num)
        return NewList[:stopNum]
    else:
        return []