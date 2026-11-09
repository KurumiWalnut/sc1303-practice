## The problem: overlapping subproblems

```python
def fibo(n):
    if n == 0 or n == 1:
        return n
    return fibo(n - 1) + fibo(n - 2)
```

`fibo(n - 1)` already works out `fibo(n - 2)`, and then `fibo(n - 2)` is computed **again**. The number of calls roughly doubles every time `n` goes up by 1, so this is **O(2ᴺ)**. `fibo(40)` makes over 300 million calls.

When the same subproblem is solved many times, the problem has **overlapping subproblems**, and dynamic programming can help.

## Memoization: remember each answer

Keep a hash table (the **memo**) from input to answer. Before computing, check it; after computing, store the result.

```python
def fibo(n, memo):
    if n == 0 or n == 1:
        return n
    if n not in memo:
        memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]

fibo(50, {})     # 12586269025
```

Each `n` is now computed **once**, so this is **O(N)** time and O(N) memory for the memo.

Pass the **same** dict down through every call. A new `{}` in each call would remember nothing.

## A default memo without the trap

```python
def fibo(n, memo=None):
    if memo is None:
        memo = {}
    ...
```

Or let Python do the memoizing:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibo(n):
    return n if n < 2 else fibo(n - 1) + fibo(n - 2)
```

## Golomb sequence (Week 9, exercise 4)

```python
def golomb(n, memo):
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo)
    return memo[n]
```

You don't need to understand the sequence. Any recursive function whose answer depends only on its inputs can be memoized the same way.

## Grids and strings

When the state has two parts, such as a grid cell `(row, col)` or two string positions `(i, j)`, use a **tuple** as the memo key: `memo[(row, col)]`. The number of different states tells you the running time.

## Top-down vs bottom-up

| | Top-down (memoization) | Bottom-up (tabulation) |
|---|---|---|
| How | recursion + memo | a loop that fills a table from the base cases up |
| Computes | only the states it needs | every state |
| Python risk | deep recursion can hit the ~1000-call limit | none |

```python
def fibo(n):                 # bottom-up, O(1) memory
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```
