def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    
    longest = ""
    for i in range(n - k + 1):
        current = ''.join(strarr[i:i+k])
        if len(current) > len(longest):
            longest = current
    
    return longest
