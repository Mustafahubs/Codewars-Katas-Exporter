def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    possitive = []
    negitive = []
    for n in arr:
        if n > 0:
            possitive.append(n)
        if n < 0:
            negitive.append(n)
    countPossitive = len(possitive)
    sumNegitivev = sum(negitive)
    return [countPossitive,sumNegitivev]