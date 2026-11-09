def partition(array, low, high):
    pivot = array[high]
    a, b = low, high - 1
    while True:
        while array[a] < pivot:              # stops on a value >= pivot (the pivot itself stops it)
            a += 1
        while b > a and array[b] > pivot:    # stops on a value <= pivot, or on reaching a
            b -= 1
        if a >= b:                           # the pointers have met
            break
        array[a], array[b] = array[b], array[a]
        a += 1
    array[a], array[high] = array[high], array[a]   # pivot into its final place
    return a
