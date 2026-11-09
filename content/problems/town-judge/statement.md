A town has `n` people, labelled `1` to `n`. `trust[i] = [a, b]` means person `a` trusts person `b`. The **town judge**, if there is one:

1. trusts nobody, and
2. is trusted by everybody else.

Write `find_judge(n, trust)` that returns the judge's label, or `-1` if there isn't exactly one person who fits.

### Examples

```text
find_judge(2, [[1, 2]])                    →  2
find_judge(3, [[1, 3], [2, 3]])            →  3
find_judge(3, [[1, 3], [2, 3], [3, 1]])    →  -1
```

### Constraints

- `1 <= n <= 1000`; up to 10 000 trust pairs, with no repeats and nobody trusting themselves.
