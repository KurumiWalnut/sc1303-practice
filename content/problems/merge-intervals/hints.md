1. **Sort** by start.
2. Go through them in order. If the next interval starts **at or before** the end of the last merged one, extend that end to `max(end, next end)`. Otherwise start a new merged interval.

Sorting is O(N log N); the merge pass is O(N).
