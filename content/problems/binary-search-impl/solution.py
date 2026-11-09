def binary_search(array, target):
    low, high = 0, len(array) - 1          # target can only be in array[low..high]
    while low <= high:                     # the range isn't empty yet
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            low = mid + 1                  # throw away the left half
        else:
            high = mid - 1                 # throw away the right half
    return -1
