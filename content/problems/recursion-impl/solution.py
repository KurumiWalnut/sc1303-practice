def sum_range(low, high):
    if low > high:                        # empty range
        return 0
    return low + sum_range(low + 1, high)


def double_array(array, index=0):
    if index >= len(array):
        return
    array[index] *= 2
    double_array(array, index + 1)


def index_of_x(string):
    if string[0] == "x":
        return 0
    return 1 + index_of_x(string[1:])


def add_until_100(array):
    if not array:
        return 0
    rest = add_until_100(array[1:])       # one call, used twice
    if array[0] + rest > 100:
        return rest
    return array[0] + rest
