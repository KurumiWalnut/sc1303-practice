import random


def median(nums):
    a = list(nums)
    k = len(a) // 2
    low, high = 0, len(a) - 1
    while True:
        r = random.randint(low, high)           # random pivot: no bad worst case on sorted input
        a[r], a[high] = a[high], a[r]
        pivot, b = a[high], low
        for i in range(low, high):
            if a[i] < pivot:
                a[i], a[b] = a[b], a[i]
                b += 1
        a[b], a[high] = a[high], a[b]
        if b == k:
            return a[b]
        if k < b:
            high = b - 1
        else:
            low = b + 1
