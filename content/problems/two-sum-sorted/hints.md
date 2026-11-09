Checking every pair is O(N²). Because the list is sorted, use **two pointers**: start at both ends.

---

If the sum is too small, move the left pointer right; if it's too big, move the right pointer left. Each step rules out one number, so it's O(N).
