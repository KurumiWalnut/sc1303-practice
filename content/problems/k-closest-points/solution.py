import random


def k_closest(points, k):
    pts = [p for p in points]
    dist = lambda p: p[0] * p[0] + p[1] * p[1]
    low, high = 0, len(pts) - 1
    while low < high:                         # quickselect until index k - 1 is in place
        r = random.randint(low, high)
        pts[r], pts[high] = pts[high], pts[r]
        pivot, b = dist(pts[high]), low
        for i in range(low, high):
            if dist(pts[i]) < pivot:
                pts[i], pts[b] = pts[b], pts[i]
                b += 1
        pts[b], pts[high] = pts[high], pts[b]
        if b == k - 1:
            break
        if b < k - 1:
            low = b + 1
        else:
            high = b - 1
    return pts[:k]
