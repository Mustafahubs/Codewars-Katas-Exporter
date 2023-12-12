def stray(arr):
    result = 0
    for num in arr:
        if arr.count(num) == 1:
            return num