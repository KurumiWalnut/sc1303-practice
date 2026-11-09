def partition(array, low, high):
    pivot = array[high]
    b = low                                   # where the next smaller value goes
    for a in range(low, high):
        if array[a] < pivot:
            array[a], array[b] = array[b], array[a]
            b += 1
    array[b], array[high] = array[high], array[b]   # pivot into its final place
    return b
