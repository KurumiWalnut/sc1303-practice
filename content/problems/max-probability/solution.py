import heapq


def max_probability(n, edges, succ_prob, start, end):
    adj = [[] for _ in range(n)]
    for (a, b), p in zip(edges, succ_prob):
        adj[a].append((b, p))
        adj[b].append((a, p))
    best = [0.0] * n
    best[start] = 1.0
    heap = [(-1.0, start)]
    while heap:
        neg, u = heapq.heappop(heap)
        prob = -neg
        if u == end:
            return prob
        if prob < best[u]:
            continue
        for v, p in adj[u]:
            if prob * p > best[v]:
                best[v] = prob * p
                heapq.heappush(heap, (-best[v], v))
    return 0.0
