## Graphs in one minute

A **graph** is a set of vertices joined by edges. Unlike a tree, a graph can have cycles, and there can be several paths between two vertices.

- **Undirected:** friendship. A–B means B–A too.
- **Directed:** following. A → B doesn't mean B → A.
- **Weighted:** each edge has a cost (see Dijkstra).

There are two common ways to store a graph:

```python
# Adjacency list as a dict
friends = {"Alice": ["Bob", "Diana"], "Bob": ["Alice"], "Diana": ["Alice"]}

# Vertex objects (the course's style)
class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)
```

## The golden rule: track what you've visited

Graphs can have cycles, so a search with no record of visited vertices goes round forever. Use a dict (`visited[v] = True`) or a set. Both give O(1) lookups.

## Depth-first search (DFS)

Go as deep as possible along one path, then back up and try the next branch. The call stack does the backing up for you.

```python
def dfs(vertex, visited):
    visited[vertex] = True
    print(vertex.value)
    for neighbour in vertex.adjacent_vertices:
        if neighbour not in visited:
            dfs(neighbour, visited)
```

## Breadth-first search (BFS)

Visit every neighbour first, then their neighbours, and so on, in rings around the start. BFS uses a **queue** instead of recursion.

```python
from collections import deque

def bfs(start):
    visited = {start: True}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        print(current.value)
        for neighbour in current.adjacent_vertices:
            if neighbour not in visited:
                visited[neighbour] = True     # mark when queued, not when printed
                queue.append(neighbour)
```

Use `deque.popleft()`, not `list.pop(0)`. The list version is O(N) for every removal.

## Which one?

| You want to… | Use |
|---|---|
| Check whether B can be reached from A, or count connected groups | Either (DFS is shorter to write) |
| Find the fewest edges from A to B | **BFS**, because it reaches closer vertices first |
| Search very long paths (thousands of vertices deep) | **BFS**, or DFS with your own stack. Recursive DFS hits Python's recursion limit (about 1 000) |

Both are **O(V + E)**: each vertex is visited once and each edge is checked once.

## Grids are graphs too

In a grid, each cell is a vertex, and its up, down, left and right neighbours are its edges. *Number of islands* asks you to count the connected groups of land cells.

```python
for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    r2, c2 = r + dr, c + dc
    if 0 <= r2 < rows and 0 <= c2 < cols and grid[r2][c2] == "1":
        ...
```

## Common bugs

- Marking a vertex as visited when you *take it out of* the queue instead of when you *add it*. The same vertex then gets queued many times.
- Ignoring neighbour order. The visiting order follows the order in `adjacent_vertices`, and the tests expect exactly that.
- Undirected graphs need each edge added **both ways**.

## BFS from many starts at once

If several cells start "infected" (as in *Rotting Oranges*), put **all** of them in the queue at the start. BFS then spreads out from all of them together, one ring per minute. The answer is the number of rings, which is O(rows × cols) in total. Simulating minute by minute and rescanning the whole grid each time is much slower.

## Directed graphs: is there a cycle?

*Course Schedule* asks whether you can take every course when some courses must come before others. That works exactly when the directed graph has **no cycle**.

**Kahn's algorithm** (BFS on in-degrees) avoids deep recursion:

1. Count each vertex's **in-degree** (how many prerequisites it has).
2. Queue every vertex with in-degree 0.
3. Pop a vertex and "take" it. Subtract 1 from the in-degree of each vertex it points to, and queue any that drop to 0.
4. If you took every vertex, there's no cycle. Any vertex left over sits on, or behind, a cycle.

The order you take them in is a **topological order**. Recursive DFS works too: a vertex you meet again while it's still on the current path means a cycle. But a long chain of prerequisites goes past Python's recursion limit.
