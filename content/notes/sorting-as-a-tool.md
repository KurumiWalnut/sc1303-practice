## Sort first, then think

Many problems become easy once the data is **in order**:

- **Duplicates** end up next to each other.
- **Intervals** sorted by start can be processed left to right.
- **Two pointers** work on sorted data.

Python's `sorted()` and `list.sort()` are O(N log N) and **stable**. In LeetCode-style questions you can use them, unless the question says you can't.

## Custom orders

```python
sorted(words, key=len)                         # by length
sorted(people, key=lambda p: (-p.age, p.name)) # age high to low, then name A to Z
```

When the order depends on comparing **two** items with each other, use `functools.cmp_to_key`. A comparison function returns a negative number if `a` should come first, positive if `b` should, and 0 if it's a tie:

```python
from functools import cmp_to_key

def compare(a, b):                 # Largest Number: which order makes the bigger string?
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0

sorted(["3", "30", "34", "5", "9"], key=cmp_to_key(compare))   # ['9', '5', '34', '3', '30']
```

## Merging intervals (Week 7, exercise 6)

1. Sort by start.
2. Go left to right. If an interval starts **before or at** the end of the last merged one, extend that end (`max` of the two ends). Otherwise start a new merged interval.

```text
[[2, 6], [15, 18], [8, 10], [1, 3]]  →  sorted: [1, 3], [2, 6], [8, 10], [15, 18]
                                      →  merged: [1, 6], [8, 10], [15, 18]
```

## How many rooms at once?

To find how many intervals overlap at the busiest moment, sort all the **start** times and all the **end** times separately. Sweep through them in time order: a start adds one, an end takes one away. The highest count is the answer. Ties need care: decide whether a meeting ending at 10 and one starting at 10 overlap.

## Sometimes you don't need to sort

- **Contains duplicate:** a set is O(N), faster than sorting. With small value ranges (ratings 0 to 10, Week 7 exercise 5), a counting array of 11 slots is O(N) too.
- **Anagram check:** compare letter counts (`Counter`) in O(N) instead of `sorted(a) == sorted(b)` in O(N log N).

Sorting is the reliable general tool. Hashing is often the faster shortcut.
