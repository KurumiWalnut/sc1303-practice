from collections import deque


def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    grid = [row[:] for row in grid]                  # don't change the caller's grid
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while queue and fresh:
        minutes += 1
        for _ in range(len(queue)):                  # one ring = one minute
            r, c = queue.popleft()
            for r2, c2 in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= r2 < rows and 0 <= c2 < cols and grid[r2][c2] == 1:
                    grid[r2][c2] = 2
                    fresh -= 1
                    queue.append((r2, c2))
    return minutes if fresh == 0 else -1
