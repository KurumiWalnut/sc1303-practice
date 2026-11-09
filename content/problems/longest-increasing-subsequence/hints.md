Let `dp[i]` = the length of the longest increasing subsequence that **ends at index `i`**.

---

Then

```text
dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i])     (or 1 if there's no such j)
```

and the answer is `max(dp)`. That's O(N²), fast enough here. (There's also an O(N log N) method using binary search.)
