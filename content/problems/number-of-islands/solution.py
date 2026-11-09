def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue
            count += 1                       # unexplored land: a new island
            grid[r][c] = "0"                 # sink it so it's never counted again
            stack = [(r, c)]
            while stack:                     # DFS with our own stack (no recursion limit)
                i, j = stack.pop()
                for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == "1":
                        grid[ni][nj] = "0"
                        stack.append((ni, nj))
    return count
