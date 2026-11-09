def bubble_sort(arr):
    comparisons = swaps = 0
    unsorted_until = len(arr) - 1           # last index of the unsorted part
    swapped = True
    while swapped and unsorted_until > 0:
        swapped = False
        for i in range(unsorted_until):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                swapped = True
        unsorted_until -= 1                 # the biggest value is now in place
    return comparisons, swaps
