def top_k_frequent(nums, k):
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
    buckets = [[] for _ in range(len(nums) + 1)]   # buckets[f] = values seen f times
    for x, f in counts.items():
        buckets[f].append(x)
    out = []
    for f in range(len(nums), 0, -1):
        for x in buckets[f]:
            out.append(x)
            if len(out) == k:
                return out
    return out
