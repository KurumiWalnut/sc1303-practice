Vertices are numbered `0` to `n - 1`, and `edges` is a list of pairs `[u, v]`. Write:

- **`build_adjacency(n, edges, directed=False)`**: a list `adj` of `n` lists, where `adj[u]` lists u's neighbours **in the order the edges appear**. If the graph is undirected, add each edge both ways.
- **`to_matrix(n, edges, directed=False)`**: an `n × n` list of lists with `1` where there's an edge and `0` elsewhere.
- **`degrees(n, edges)`**: the degree of every vertex in an **undirected** graph, as a list.
- **`in_out_degrees(n, edges)`**: for a **directed** graph, a pair of lists `(in_degree, out_degree)`.

### Example

```text
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
build_adjacency(4, edges)                  →  [[1, 2], [0, 2], [0, 1, 3], [2]]
build_adjacency(4, edges, directed=True)   →  [[1, 2], [2], [3], []]
to_matrix(3, [[0, 1]])                     →  [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
degrees(4, edges)                          →  [2, 2, 3, 1]
in_out_degrees(4, edges)                   →  ([0, 1, 2, 1], [2, 1, 1, 0])
```
