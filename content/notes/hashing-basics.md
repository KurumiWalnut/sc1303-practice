## The idea

A **hash table** stores key–value pairs in an array. A **hash function** turns the key into a number, and that number (mod the array size) is the **index** where the pair goes. Reading a key means computing its index and jumping straight there: **O(1)**, however much data there is.

Python's `dict` and `set` are hash tables.

## A toy hash function (lecture)

Number the letters A = 1, B = 2, …, add them up, then add the digits until one digit is left:

```text
"BRAND" → 2 + 18 + 1 + 14 + 4 = 39 → 3 + 9 = 12 → 1 + 2 = 3     goes in cell 3
"MODEL" → 49 → 13 → 4                                             goes in cell 4
"YEAR"  → 49 → 13 → 4                                             also cell 4: a collision!
```

A hash function must be **deterministic**: the same key always gives the same number. Real ones spread keys out much more evenly than this.

## Collisions and separate chaining

Two keys landing in the same cell is a **collision**. With **separate chaining**, each cell holds a list of `[key, value]` pairs:

```text
cell 3: [["BRAND", "Tesla"]]
cell 4: [["MODEL", "Model Y"], ["YEAR", 2022]]
```

To look up `"YEAR"`, jump to cell 4, then search that short list linearly. If every key collided, everything would sit in one list and lookups would be **O(N)**: the worst case. A good table keeps the lists short.

```python
class HashTable:
    def __init__(self, capacity=10):
        self.buckets = [[] for _ in range(capacity)]

    def put(self, key, value):
        bucket = self.buckets[hash(key) % len(self.buckets)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value          # key already there: overwrite
                return
        bucket.append([key, value])
```

## Load factor and resizing

**Load factor** = entries ÷ cells. The rule of thumb from the lecture: about **7 entries for every 10 cells (0.7)**.

When the load factor goes above 0.7, make a bigger array (for example, twice the size) and **rehash** every pair into it. The index depends on the array size, so pairs can't just be copied across. Resizing is O(N), but it happens rarely enough that inserts are still **O(1) on average**.

## Where hash tables beat arrays

| Task | Array | Hash table |
|---|---|---|
| Look up by key | O(N) search | **O(1)** |
| Is x present? | O(N) | **O(1)** with a set |
| Is array A a subset of B? | O(N·M) nested loops | **O(N + M)**: put B in a set |

## Using a set as a "seen" table

*Longest Consecutive Sequence*: put every number in a set. Only start counting at numbers where `x - 1` is **not** in the set (the start of a run), then count up while `x + 1` is in the set. Each number is looked at a constant number of times: O(N).

*Happy Number*: keep a set of the numbers you've already seen. If one comes round again, you're in a loop.

## Common bugs

- Not overwriting an existing key, so it ends up stored twice.
- Resizing without rehashing (copying the old buckets across as they are).
- Using a list for "have I seen this?" checks: `x in some_list` is O(N).
