def maximal_network_rank(n, roads):
    degree = [0] * n
    connected = set()
    for a, b in roads:
        degree[a] += 1
        degree[b] += 1
        connected.add((a, b))
        connected.add((b, a))
    best = 0
    for a in range(n):
        for b in range(a + 1, n):
            rank = degree[a] + degree[b] - ((a, b) in connected)
            best = max(best, rank)
    return best
