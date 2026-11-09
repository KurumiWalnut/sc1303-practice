def min_groups(intervals):
    starts = sorted(a for a, b in intervals)
    ends = sorted(b for a, b in intervals)
    open_now = best = 0
    j = 0
    for s in starts:
        while ends[j] < s:                # finished before this one starts
            open_now -= 1
            j += 1
        open_now += 1
        best = max(best, open_now)
    return best
