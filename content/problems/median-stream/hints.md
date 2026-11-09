Sorting on every `find_median` call is too slow for 100 000 operations. Use **two heaps**: one for the smaller half of the numbers and one for the larger half.

---

The two heaps:

- a **max-heap** for the smaller half (with `heapq`, push `-num`),
- a **min-heap** for the larger half,

and keep their sizes equal, or the max-heap one bigger. The median is then at the top of one or both heaps.
