def running_medians(nums):
    ordered, out = [], []
    for x in nums:
        low, high = 0, len(ordered)               # binary search for the gap
        while low < high:
            mid = (low + high) // 2
            if ordered[mid] <= x:
                low = mid + 1
            else:
                high = mid
        ordered.insert(low, x)                    # the shift step of insertion sort
        n = len(ordered)
        if n % 2:
            out.append(float(ordered[n // 2]))
        else:
            out.append((ordered[n // 2 - 1] + ordered[n // 2]) / 2)
    return out
