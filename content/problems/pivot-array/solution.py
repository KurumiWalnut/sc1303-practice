def pivot_array(nums, pivot):
    less, equal, greater = [], [], []
    for x in nums:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return less + equal + greater
