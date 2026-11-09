import heapq


def kth_largest(nums, k):
    top_k = []                          # min-heap holding the k largest values seen so far
    for x in nums:
        heapq.heappush(top_k, x)
        if len(top_k) > k:
            heapq.heappop(top_k)        # drop the smallest: it can't be in the top k
    return top_k[0]                     # smallest of the top k = k-th largest
