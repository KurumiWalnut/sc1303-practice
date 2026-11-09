The course exercise uses positive numbers only, so the answer is simply the three biggest. Here the numbers can be **negative**: two very negative numbers multiply to a big positive one.

---

So the answer is the larger of:

- the three largest numbers multiplied together, and
- the two smallest (most negative) numbers times the largest.

Sorting makes this O(N log N). One pass that tracks the top three and bottom two makes it O(N). Trying every triple is O(N³), which is far too slow for 10 000 numbers.
