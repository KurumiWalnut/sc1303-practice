Binary search still works. At each step, **one half is sorted**: if `nums[low] <= nums[mid]`, the left half is sorted, otherwise the right half is.

---

Check whether `target` is inside the sorted half's range. If so, search there; if not, search the other half.
