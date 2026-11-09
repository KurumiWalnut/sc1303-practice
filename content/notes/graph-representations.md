## Words you'll need

- **Vertex** (node) and **edge** (a connection between two vertices).
- **Undirected:** an edge goes both ways (friendship). **Directed:** an edge has a direction (following someone).
- **Weighted:** every edge has a number, such as a price or a distance.
- **Degree:** how many edges touch a vertex. In a directed graph there's an **in-degree** (edges coming in) and an **out-degree** (edges going out).

## Four ways to write a graph down

**1. Edge list:** what most questions give you.

```python
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
```

**2. Adjacency list:** for each vertex, the list of its neighbours. This is the usual choice.

```python
adj = [[] for _ in range(n)]          # or a dict: {vertex: [neighbours]}
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)                  # undirected: add it both ways
```

**3. Adjacency matrix:** an n × n grid where `matrix[u][v]` is 1 (or the weight) if there's an edge.

```python
matrix = [[0] * n for _ in range(n)]  # NOT [[0] * n] * n: that repeats ONE row n times
for u, v in edges:
    matrix[u][v] = matrix[v][u] = 1
```

**4. Vertex objects** (the course's `graph_template.py`): each `Vertex` keeps a list `adjacent_vertices`.

## Which one?

| | Adjacency list | Adjacency matrix |
|---|---|---|
| Memory | **O(V + E)** | O(V²) |
| Is u–v an edge? | O(degree of u), or O(1) with sets | **O(1)** |
| Loop over u's neighbours | **O(degree of u)** | O(V) |
| Good for | sparse graphs (most real ones) | small or dense graphs |

Most graphs in questions are **sparse** (E is much smaller than V²), so use an adjacency list.

## Degrees from an edge list

You often don't need the whole graph, just a count per vertex:

```python
indeg, outdeg = [0] * n, [0] * n
for u, v in edges:          # directed edge u → v
    outdeg[u] += 1
    indeg[v] += 1
```

*Find the Town Judge* is just this: the judge trusts nobody (out-degree 0) and is trusted by everyone else (in-degree n − 1).

## Common bugs

- `[[0] * n] * n`: every row is the **same** list, so setting one cell changes the whole column.
- Forgetting the second direction in an undirected graph.
- Vertices numbered from 1 in the question but stored from 0 in your list (or the other way round).
- A vertex with no edges is still a vertex. It must be in your adjacency list, with an empty list.
