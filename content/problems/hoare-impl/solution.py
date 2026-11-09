def partition(array, low, high):
    pivot = array[high]                      # the pivot is the last element
    a, b = low, high - 1
    while True:
        while a <= b and array[a] <= pivot:  # a stops on a value bigger than the pivot
            a += 1
        while a <= b and array[b] >= pivot:  # b stops on a value smaller than the pivot
            b -= 1
        if a < b:                            # both stopped: swap the two values
            array[a], array[b] = array[b], array[a]
        else:                                # the pointers have met or crossed
            break
    array[a], array[high] = array[high], array[a]   # pivot into its final place
    return a
