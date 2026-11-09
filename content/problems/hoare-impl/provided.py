def quick_sort(array, low, high):
    """The course's quicksort. It calls your partition."""
    if low < high:
        p = partition(array, low, high)
        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)
