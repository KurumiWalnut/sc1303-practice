Fill `nums1` from the **back**.

---

Compare the largest remaining values of the two lists and put the larger one in the last free slot. Working backwards means you never overwrite a value you still need. That's O(m + n).
