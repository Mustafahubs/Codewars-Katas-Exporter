def first_non_consecutive(arr):
    sortedArr = sorted(arr)
    firstN,secondN = sortedArr[0],sortedArr[-1]
    goodArr = list(range(firstN,secondN+1))
    for gn,n in zip(goodArr,arr):
        if gn != n:
            return n
    else:
        return None