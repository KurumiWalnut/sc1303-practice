Greedy (biggest coin first) can fail: with coins `[1, 3, 4]` and amount 6, greedy gives 4 + 1 + 1, but 3 + 3 is better.

---

Let `dp[a]` = the fewest coins that make `a`. Then `dp[0] = 0` and `dp[a] = 1 + min(dp[a - c])` over the coins `c <= a`. Fill it **bottom-up** from 1 to `amount`: top-down recursion would go 10 000 calls deep, past Python's limit.
