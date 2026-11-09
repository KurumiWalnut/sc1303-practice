`Node` (with `data` and `next`), `build_list` and `to_pylist` are already loaded (see **Provided code**).

Write `is_palindrome(head)` that returns `True` if the list reads the same forwards and backwards. An empty list is a palindrome.

### Examples

```text
is_palindrome(build_list([1, 2, 2, 1]))   →  True
is_palindrome(build_list([1, 2]))         →  False
```

### Constraints

- Up to 100 000 nodes. Recursion that goes one level per node is too deep for Python.
