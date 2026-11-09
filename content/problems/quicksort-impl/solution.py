def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:                          # 0 or 1 elements: already sorted
        p = partition(array, low, high)
        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)


def quickselect(array, k, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low == high:
        return array[low]
    p = partition(array, low, high)
    if k == p:
        return array[p]
    if k < p:
        return quickselect(array, k, low, p - 1)
    return quickselect(array, k, p + 1, high)
