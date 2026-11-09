Taking `max()` of every window is O(N·k). Keep a `deque` of **indexes** whose values are **decreasing** from front to back.

---

1. Before adding index `i`, pop from the **back** every index whose value is ≤ `nums[i]`. They can never be a maximum again.
2. Append `i`.
3. If the front index has slid out of the window (`<= i - k`), pop it from the **front**.
4. Once `i >= k - 1`, the front is the maximum of the current window.

Each index is added and removed at most once: O(N).
