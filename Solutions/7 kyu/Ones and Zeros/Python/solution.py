def binary_array_to_number(arr):
    count = 0
    length_arr = len(arr)
    
    for i in range(length_arr):
        count += arr[i] * (2 ** (length_arr - i - 1))
    
    return count