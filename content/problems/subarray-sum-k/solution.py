def subarray_sum(nums, k):
    seen = {0: 1}                      # running total -> how many times it has appeared
    prefix = count = 0
    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count
