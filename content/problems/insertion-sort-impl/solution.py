def insertion_sort(arr):
    comparisons = shifts = 0
    for i in range(1, len(arr)):
        temp = arr[i]
        pos = i - 1
        while pos >= 0:
            comparisons += 1
            if arr[pos] > temp:
                arr[pos + 1] = arr[pos]       # shift right
                shifts += 1
                pos -= 1
            else:
                break
        arr[pos + 1] = temp                   # insert into the gap
    return comparisons, shifts
