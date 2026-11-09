def majority_element(nums):
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
        if counts[x] > len(nums) // 2:
            return x
