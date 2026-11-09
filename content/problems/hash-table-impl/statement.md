Build a hash table that handles collisions with **separate chaining**. `hash_key(key)` is already loaded (see **Provided code**); a key's cell is `hash_key(key) % len(self.buckets)`.

- `self.buckets` is a list of cells. Each cell is a list of `[key, value]` pairs, in the order they were added.
- `self.count` is the number of keys stored.

Write:

- **`put(key, value)`**: if the key is already in its cell, replace its value. Otherwise append `[key, value]` to the cell and add 1 to `count`. Then, if `count / len(self.buckets) > 0.7`, **resize**.
- **`get(key)`**: the key's value, or `None` if it isn't there.
- **`remove(key)`**: delete the key's pair and return `True`, or return `False` if it isn't there.
- **`__len__()`**: the number of keys.
- **`_resize()`**: replace `buckets` with **twice as many** empty cells, then put every old pair back. Go through the old cells in order and each cell's pairs in order, appending each pair to its **new** cell.

### Example

```text
t = HashTable(10)
t.put(3, "a"); t.put(13, "b"); t.put(23, "c")     # all land in cell 3
t.buckets[3]          →  [[3, 'a'], [13, 'b'], [23, 'c']]
t.get(13)             →  'b'

t = HashTable(10)
for k in range(8): t.put(k, k)    # the 8th key makes the load factor 0.8
len(t.buckets)        →  20
```
