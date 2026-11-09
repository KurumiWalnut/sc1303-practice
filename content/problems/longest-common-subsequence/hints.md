Use a table: `dp[i][j]` = the answer for the first `i` letters of `text1` and the first `j` letters of `text2`.

---

Row 0 and column 0 are 0. Then

```text
if text1[i-1] == text2[j-1]:  dp[i][j] = dp[i-1][j-1] + 1
else:                         dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

and the answer is `dp[len(text1)][len(text2)]`. Fill it bottom-up, row by row (only the previous row is needed).
