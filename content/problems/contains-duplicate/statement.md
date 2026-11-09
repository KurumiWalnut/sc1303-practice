Write `contains_duplicate(nums)` that returns `True` if any value appears **at least twice**.

> [!PROF-NOTE] Week 7 seminar notebook, has_duplicate
>
> The seminar's `has_duplicate` marks values in a list of 11 slots, so it only works when every value is between 0 and 10. Here values can be anything, so use a set, or sort first and compare neighbours.

### Examples

```text
contains_duplicate([1, 2, 3, 1])                    →  True
contains_duplicate([1, 2, 3, 4])                    →  False
contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])  →  True
```
