Squaring then sorting is O(N log N). For O(N): the **largest** square is always at one of the two ends (a very negative number or a big positive one).

---

Put two pointers at the ends, and fill the answer from the **back** with the bigger square, moving that pointer inwards.
