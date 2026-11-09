Use a **min-heap** (`heapq`) holding one entry per list: `(value, list index, position)`. Pop the smallest value, add it to the answer, then push the next value from the same list. That's O(N log k) for N values in total.

Scanning all k lists for the smallest head every time is O(N · k), too slow when k is in the thousands.
