Compare squared distances `x*x + y*y`: there's no need for square roots.

---

Sorting by distance is O(N log N). Quickselect on the distances gets the closest `k` into the first `k` slots in O(N) on average. A heap of size `k` is O(N log k).
