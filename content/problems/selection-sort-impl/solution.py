def selection_sort(arr):
    comparisons = swaps = 0
    for i in range(len(arr) - 1):
        lowest = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[lowest]:
                lowest = j
        if lowest != i:                       # only swap when needed
            arr[i], arr[lowest] = arr[lowest], arr[i]
            swaps += 1
    return comparisons, swaps
