def linear_search(arr, target):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return i, steps
    return -1, steps


def insert_at(arr, index, value):
    arr.append(None)                          # room for one more
    shifts = 0
    for j in range(len(arr) - 1, index, -1):  # shift from the back
        arr[j] = arr[j - 1]
        shifts += 1
    arr[index] = value
    return shifts


def delete_by_value(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            shifts = 0
            for j in range(i, len(arr) - 1):  # close the gap
                arr[j] = arr[j + 1]
                shifts += 1
            arr.pop()                         # the last slot is now a copy
            return shifts
    return "Value not found"


def reverse_array(arr):
    left, right, swaps = 0, len(arr) - 1, 0
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        swaps += 1
        left += 1
        right -= 1
    return swaps
