There are `num_courses` courses, numbered `0` to `num_courses - 1`. `prerequisites[i] = [a, b]` means you must take course `b` **before** course `a`. Write `can_finish(num_courses, prerequisites)` that returns `True` if you can take every course.

### Examples

```text
can_finish(2, [[1, 0]])            →  True    (take 0, then 1)
can_finish(2, [[1, 0], [0, 1]])    →  False   (each needs the other first)
```

### Constraints

- `1 <= num_courses <= 2000`; up to 5 000 prerequisite pairs, with no repeats.
- Prerequisite chains can be up to 2 000 courses long, which is too deep for recursion in Python.
