def sort_array_by_parity(nums):
    b = 0
    for a in range(len(nums)):
        if nums[a] % 2 == 0:                  # "smaller than the pivot" becomes "is even"
            nums[a], nums[b] = nums[b], nums[a]
            b += 1
    return nums
