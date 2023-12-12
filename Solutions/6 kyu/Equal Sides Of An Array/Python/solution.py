def find_even_index(arr):
    n = len(arr)
    total_sum = sum(arr)
    left_sum = 0
    for i in range(n):
        if left_sum == total_sum - left_sum - arr[i]:
            return i
        left_sum += arr[i]
    return -1
