def two_sum(numbers, target):
    for xIndex,x in enumerate(numbers):
        for yIndex,y in enumerate(numbers):
            if xIndex != yIndex:
                result = x + y
                if result == target:
                    return xIndex,yIndex