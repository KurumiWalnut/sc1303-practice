Design a **least-recently-used (LRU) cache** with a fixed capacity.

- `LRUCache(capacity)` creates an empty cache.
- `get(key)` returns the value for `key`, or `-1` if it isn't there. A successful `get` counts as using the key.
- `put(key, value)` inserts or updates `key` (this also counts as using it). If the cache is then over capacity, remove the **least recently used** key.

Both operations should be **O(1)**.

### Example

```text
c = LRUCache(2)
c.put(1, 1); c.put(2, 2)
c.get(1)     →  1
c.put(3, 3)            # removes key 2 (least recently used)
c.get(2)     →  -1
c.put(4, 4)            # removes key 1
c.get(1)     →  -1
c.get(3)     →  3
c.get(4)     →  4
```

### Constraints

- `1 ≤ capacity ≤ 20 000`; up to 200 000 calls.
