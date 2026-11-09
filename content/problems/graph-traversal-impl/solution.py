from collections import deque


def dfs_order(start):
    order = []
    visited = {}

    def visit(vertex):
        visited[vertex] = True
        order.append(vertex.value)
        for neighbour in vertex.adjacent_vertices:
            if neighbour not in visited:
                visit(neighbour)

    visit(start)
    return order


def bfs_order(start):
    order = []
    visited = {start: True}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        order.append(current.value)
        for neighbour in current.adjacent_vertices:
            if neighbour not in visited:
                visited[neighbour] = True     # mark when queued so it's never queued twice
                queue.append(neighbour)
    return order
