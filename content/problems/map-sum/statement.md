The tests drive your class through `run_ops` (see **Provided code**), which creates one object, runs the operations in order and returns what the query operations returned.

Write a class `MapSum` with:

- **`insert(key, val)`**: store `key` with the number `val`. If `key` is already there, its old value is **replaced**.
- **`sum(prefix)`**: return the total of the values of every key that starts with `prefix`.

### Example

```text
insert("apple", 3)
sum("ap")      →  3
insert("app", 2)
sum("ap")      →  5
insert("apple", 1)    (replaces 3)
sum("ap")      →  3
```

### Constraints

- Up to 60 000 calls; keys have at most 10 lowercase letters; `1 <= val <= 1000`.
