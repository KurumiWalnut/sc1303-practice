from collections import deque


def valid_path(n, edges, source, destination):
    neighbours = {v: [] for v in range(n)}
    for u, v in edges:
        neighbours[u].append(v)          # undirected: add the edge both ways
        neighbours[v].append(u)

    visited = {source: True}
    queue = deque([source])
    while queue:
        current = queue.popleft()
        if current == destination:
            return True
        for nxt in neighbours[current]:
            if nxt not in visited:
                visited[nxt] = True
                queue.append(nxt)
    return False
