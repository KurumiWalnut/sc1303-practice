def intersection(nums1, nums2):
    first = set(nums1)
    return list({x for x in nums2 if x in first})
