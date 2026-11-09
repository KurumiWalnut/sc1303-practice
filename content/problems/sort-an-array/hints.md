The plain course quicksort (last element as pivot) isn't enough here. Think about which inputs make its partitions lopsided.

---

The plain course quicksort isn't enough because:

- **Already sorted** input makes every partition lopsided: O(N²) time and N levels of recursion, past Python's limit. Pick a **random pivot**.
- **Lots of equal values** (even all the same) are lopsided too with a two-way partition. Use a **three-way partition**: less than, equal to and greater than the pivot. Then recurse on the "less" and "greater" parts only.

(Merge sort is also O(N log N) every time, if you'd rather write that.)
