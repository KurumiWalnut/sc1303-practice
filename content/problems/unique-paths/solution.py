def unique_paths(m, n):
    row = [1] * n                         # the top row: one path to each cell
    for _ in range(1, m):
        for c in range(1, n):
            row[c] += row[c - 1]          # from above (old row[c]) + from the left
    return row[-1]
