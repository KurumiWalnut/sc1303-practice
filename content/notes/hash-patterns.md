## The big idea

Whenever you write a nested loop to **look for** something, ask: could a dict or set answer that question in O(1)? Swapping the inner loop for a lookup often turns O(N²) into **O(N)**.

## Pattern 1: "have I seen what I need?" (Two Sum)

Walk through the list once. For each number, the partner you need is `target - x`. Check whether you've already seen it, then remember `x` and its index.

```python
def two_sum(nums, target):
    seen = {}                        # value -> index
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
```

Check **before** storing, so an element is never paired with itself.

## Pattern 2: counting

```python
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1

from collections import Counter     # the same thing, built in
counts = Counter(nums)
```

- **Majority element:** the key whose count is more than n/2.
- **Top k frequent:** count, then take the k biggest counts. `sorted(counts, key=counts.get, reverse=True)[:k]` is O(N log N). **Bucket sort** by frequency is O(N): `buckets[f]` lists the values that appear exactly `f` times, and you read from the highest `f` down.

## Pattern 3: set operations

```python
set(a) & set(b)       # intersection: in both
set(a) | set(b)       # union: in either
set(a) - set(b)       # in a but not in b
```

Each one is O(len(a) + len(b)). Remember: a set has **no duplicates** and **no order**.

## Pattern 4: prefix sums + counts (Subarray Sum Equals K)

Let `prefix` be the running total. A subarray ending here sums to `k` exactly when some **earlier** running total equals `prefix - k`. Keep a dict of how many times each running total has appeared:

```python
def subarray_sum(nums, k):
    count, prefix = 0, 0
    seen = {0: 1}                    # the empty prefix
    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count
```

This works with negative numbers too, which a sliding window can't handle.

## What can be a key?

Keys must be **hashable** (unchangeable): numbers, strings and tuples work; lists don't. To group by "the same letters", use `tuple(sorted(word))` or a tuple of letter counts as the key.

## Common bugs

- Pairing an element with itself in Two Sum.
- Starting the prefix-sum dict empty instead of `{0: 1}`, which misses subarrays that start at index 0.
- Expecting a set or dict to keep things sorted.
