The `Vertex` class from the lectures is already loaded (see **Provided code** below). Each vertex has a `value` and a list `adjacent_vertices`.

Write two functions. Each returns the **values** of every vertex reachable from `start`, in the order they're visited:

- **`dfs_order(start)`**: depth-first. Visit a vertex, then recursively visit each unvisited neighbour **in the order they appear in `adjacent_vertices`**.
- **`bfs_order(start)`**: breadth-first. Use a queue. Take the front vertex, then add each unvisited neighbour to the back, in `adjacent_vertices` order.

Keep track of visited vertices with a dict or set, because graphs can have cycles.

### Example: the friends graph from `graph_template.py`

```text
Alice:   Bob, Diana, Fred         Diana: Alice, Bob, Fred
Bob:     Alice, Diana, Cynthia    Elise: Fred
Cynthia: Bob                      Fred:  Alice, Diana, Elise

dfs_order(alice)  →  ['Alice', 'Bob', 'Diana', 'Fred', 'Elise', 'Cynthia']
bfs_order(alice)  →  ['Alice', 'Bob', 'Diana', 'Fred', 'Cynthia', 'Elise']
```

The tests build graphs with the provided `build_graph({...})` helper, which adds neighbours in the order they're listed.
