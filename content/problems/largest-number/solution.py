from functools import cmp_to_key


def largest_number(nums):
    def compare(a, b):
        if a + b > b + a:
            return -1                     # a should come first
        if a + b < b + a:
            return 1
        return 0

    parts = sorted(map(str, nums), key=cmp_to_key(compare))
    result = "".join(parts)
    return "0" if result[0] == "0" else result
