def maximum_product(nums):
    s = sorted(nums)
    return max(s[-1] * s[-2] * s[-3], s[0] * s[1] * s[-1])
