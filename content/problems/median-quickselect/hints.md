You could sort, but quickselect finds it in O(N) on average: it's the value at sorted index `len(nums) // 2`. Write your own partition (the pivot can be the last element, or a random one).
