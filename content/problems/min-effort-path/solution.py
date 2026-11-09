import heapq


def minimum_effort_path(heights):
    rows, cols = len(heights), len(heights[0])
    best = [[float("inf")] * cols for _ in range(rows)]
    best[0][0] = 0
    heap = [(0, 0, 0)]
    while heap:
        effort, r, c = heapq.heappop(heap)
        if (r, c) == (rows - 1, cols - 1):
            return effort
        if effort > best[r][c]:
            continue
        for r2, c2 in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= r2 < rows and 0 <= c2 < cols:
                e = max(effort, abs(heights[r2][c2] - heights[r][c]))
                if e < best[r2][c2]:
                    best[r2][c2] = e
                    heapq.heappush(heap, (e, r2, c2))
    return 0
