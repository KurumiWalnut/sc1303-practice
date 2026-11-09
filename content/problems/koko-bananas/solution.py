def min_eating_speed(piles, h):
    low, high = 1, max(piles)
    while low < high:
        mid = (low + high) // 2
        hours = sum((p + mid - 1) // mid for p in piles)
        if hours <= h:
            high = mid                    # fast enough: try slower
        else:
            low = mid + 1                 # too slow
    return low
