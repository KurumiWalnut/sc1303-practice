def int_sqrt(n):
    low, high = 0, n
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            answer = mid          # mid works, but a bigger value might too
            low = mid + 1
        else:
            high = mid - 1        # mid is too big
    return answer
