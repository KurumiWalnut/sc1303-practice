## A recipe for DP questions

1. **State:** say in words what `dp[i]` (or `dp[i][j]`) means. For example: "the number of ways to reach step `i`".
2. **Recurrence:** how `dp[i]` is built from smaller states. Ask: *what was the last choice made?*
3. **Base cases:** the smallest states, which you know without the recurrence.
4. **Order:** fill the table so every state is computed after the states it needs.
5. **Answer:** which entry holds it. Often `dp[n]`, sometimes the max over all `i`.

If step 1 is vague, the rest won't work. Write it down before coding.

## Climbing stairs (Week 9, coding exercise 3)

You climb 1 or 2 steps at a time. The last move to step `i` came from `i - 1` or `i - 2`:

```text
ways[i] = ways[i - 1] + ways[i - 2]      ways[1] = 1, ways[2] = 2
```

That's Fibonacci again. Only the last two values are needed, so two variables are enough: O(N) time, O(1) memory.

## Min cost climbing stairs (exercise 3++)

`best[i]` = cheapest cost to **stand on** step `i`, where you can start on step 0 or step 1 for free:

```text
best[i] = min(best[i - 1] + cost[i - 1], best[i - 2] + cost[i - 2])
```

The answer is `best[n]`: the top, just past the last step.

## Coin change (fewest coins)

`dp[a]` = the fewest coins that make amount `a`. The last coin used was one of the `coins`:

```text
dp[0] = 0
dp[a] = 1 + min(dp[a - c] for c in coins if c <= a)     (infinity if none work)
```

Time O(amount × number of coins). Greedy ("always take the biggest coin") **fails**: with coins `[1, 3, 4]` and amount 6, greedy takes 4 + 1 + 1, but 3 + 3 is better.

## Longest increasing subsequence

`dp[i]` = the length of the longest increasing subsequence that **ends at** `i`:

```text
dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i])    (or 1 if there's none)
```

The answer is `max(dp)`, not `dp[-1]`. That's O(N²). There's an O(N log N) version that keeps, for each length, the smallest possible last value, and updates it with binary search (`bisect_left`).

## Two strings: a 2-D table

Longest common subsequence: `dp[i][j]` = the LCS of the first `i` letters of `a` and the first `j` letters of `b`.

```text
if a[i-1] == b[j-1]:  dp[i][j] = dp[i-1][j-1] + 1
else:                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

Row 0 and column 0 are 0 (an empty string has nothing in common). Fill row by row: O(len(a) × len(b)).

## Top-down or bottom-up?

Both have the same complexity. In Python, prefer **bottom-up** when the recursion would go deep: coin change with amount 10 000 recurses 10 000 levels, far past the ~1000 limit.

## Common bugs

- Not saying what `dp[i]` means, then mixing up "ends at i" with "within the first i".
- Off-by-one errors: a table of size `n + 1` for `n` items, with `dp[0]` as the empty case.
- Returning `dp[-1]` when the answer is the max over all states.
- Using `float("inf")` but forgetting to turn it into -1 (or whatever "impossible" should be) at the end.
