def ordered_insert(arr, value):
    steps, i = 0, 0
    while i < len(arr):
        steps += 1                        # compare
        if arr[i] > value:
            break
        i += 1
    arr.append(None)
    for j in range(len(arr) - 1, i, -1):
        arr[j] = arr[j - 1]               # shift right
        steps += 1
    arr[i] = value
    return steps + 1                      # + the insert


def ordered_search(arr, target):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return i, steps
        if arr[i] > target:
            break                         # everything after is bigger too
    return -1, steps
