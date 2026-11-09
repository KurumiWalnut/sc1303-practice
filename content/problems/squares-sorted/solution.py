def sorted_squares(nums):
    out = [0] * len(nums)
    left, right = 0, len(nums) - 1
    for write in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            out[write] = nums[left] * nums[left]
            left += 1
        else:
            out[write] = nums[right] * nums[right]
            right -= 1
    return out
