def search_range(nums, target):
    def find(leftmost):
        low, high, found = 0, len(nums) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                found = mid               # a match: keep looking further out
                if leftmost:
                    high = mid - 1
                else:
                    low = mid + 1
        return found

    return [find(True), find(False)]
