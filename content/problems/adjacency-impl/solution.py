def build_adjacency(n, edges, directed=False):
    adj = [[] for _ in range(n)]          # a separate list for every vertex
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return adj


def to_matrix(n, edges, directed=False):
    matrix = [[0] * n for _ in range(n)]  # not [[0] * n] * n, which repeats one row
    for u, v in edges:
        matrix[u][v] = 1
        if not directed:
            matrix[v][u] = 1
    return matrix


def degrees(n, edges):
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    return deg


def in_out_degrees(n, edges):
    indeg, outdeg = [0] * n, [0] * n
    for u, v in edges:
        outdeg[u] += 1
        indeg[v] += 1
    return indeg, outdeg
