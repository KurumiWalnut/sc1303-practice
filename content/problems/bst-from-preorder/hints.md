The simplest approach inserts the values one by one, in order. That works because pre-order lists each parent before its children.

---

For a faster O(N) solution, pass down an upper bound and consume the list from left to right.
