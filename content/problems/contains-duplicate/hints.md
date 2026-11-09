Comparing every pair is O(N²). Two better ways:

- **Sort** first, so equal values sit next to each other, then check neighbours: O(N log N).
- Use a **set** of values seen so far: O(N).

(The course version has ratings from 0 to 10 only, so a counting list of 11 slots also works.)
