Count with a dict, then pick the `k` biggest counts.

---

Sorting the counts is O(N log N). For O(N), use **bucket sort**: make `buckets[f]` the list of values that appear exactly `f` times, then read the buckets from the highest `f` down until you have `k` values.
