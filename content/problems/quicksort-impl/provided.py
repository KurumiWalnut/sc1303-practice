def partition(array, low, high):
    """Lomuto partition (the course version): pivot = array[high]. Returns the pivot's final index."""
    pivot = array[high]
    b = low
    for a in range(low, high):
        if array[a] < pivot:
            array[a], array[b] = array[b], array[a]
            b += 1
    array[b], array[high] = array[high], array[b]
    return b
