def kth_smallest(nums, k):
    a = list(nums)
    for i in range(k):                        # k passes only
        lowest = i
        for j in range(i + 1, len(a)):
            if a[j] < a[lowest]:
                lowest = j
        a[i], a[lowest] = a[lowest], a[i]
    return a[k - 1]
