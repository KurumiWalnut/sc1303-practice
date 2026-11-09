## What Big O answers

> If there are N data elements, how many steps will the algorithm take?

Big O describes how the step count **grows** as N grows, usually in the **worst case**. It ignores exact counts: 3N + 5 steps and N steps are both **O(N)**.

## The rules

1. **Drop constants:** O(2N) → O(N), and O(N/2) → O(N).
2. **Keep only the fastest-growing term:** O(N² + N) → O(N²).
3. **A loop inside a loop multiplies:** N × N → O(N²). **Loops one after another add:** N + N → O(N).
4. **Halving each step** (as in binary search) is **O(log N)**.

## The common classes, fastest first

| Big O | Name | Doubling N… | Example |
|---|---|---|---|
| O(1) | constant | no change | read `arr[i]`, dict lookup, a formula |
| O(log N) | logarithmic | adds **one** step | binary search |
| O(N) | linear | doubles | linear search, one pass |
| O(N log N) | linearithmic | a bit more than doubles | `sorted()`, quicksort on average |
| O(N²) | quadratic | **×4** | bubble, selection and insertion sort; checking all pairs |
| O(2ᴺ) | exponential | squares | naive recursive Fibonacci |

With N = 1 000 000, linear search can take a million steps, while binary search takes about **20**.

## Same Big O, different speed

Selection sort takes about N²/2 steps and bubble sort about N², but both are O(N²). Big O separates **classes**. Within a class, you need a closer count to tell algorithms apart.

## Best, average and worst case

Insertion sort is O(N) on sorted data and O(N²) on reversed data. When people quote one Big O, they mean the **worst case**, unless they say otherwise.

## From O(N) to O(1): the sum of even numbers (Week 5, exercise 2)

Looping to add 2 + 4 + … up to 10 000 000 takes millions of steps. But with m = N // 2 even numbers,

```text
2 + 4 + … + 2m = 2 × (1 + 2 + … + m) = m × (m + 1)
```

That's one formula: **O(1)**, whatever N is.

## Recognising faster approaches

| Slow version | Faster idea |
|---|---|
| Check every pair: O(N²) | sort, then use **two pointers**: O(N log N); or a **hash set**: O(N) |
| Re-add a window's values each time | keep a **running** total |
| Try every subarray for the best sum | **Kadane's algorithm**: the best sum ending here is `max(x, best_ending_before + x)`, one pass |
