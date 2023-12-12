def merge_arrays(arr1, arr2):
    sumlist = arr1+arr2
    store = []
    for num in sumlist:
        if num not in store:
            store.append(num)
    store.sort()
    return store