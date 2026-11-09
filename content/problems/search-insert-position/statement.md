Write `search_insert(nums, target)`.

`nums` is a list of **distinct** integers sorted in ascending order. If `target` is in `nums`, return its index. If not, return the index where it **would be inserted** to keep `nums` sorted.

Do it in **O(log N)**.

### Examples

```text
search_insert([1, 3, 5, 6], 5)  →  2    (found at index 2)
search_insert([1, 3, 5, 6], 2)  →  1    (2 goes between 1 and 3)
search_insert([1, 3, 5, 6], 7)  →  4    (7 goes at the end)
```

### Constraints

- `1 ≤ len(nums) ≤ 500 000`
- One hidden test runs 3 000 searches on a large list.
