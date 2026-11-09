These recursive functions are correct but **exponentially slow**:

```python
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

def golomb(n):
    if n == 1:
        return 1
    return 1 + golomb(n - golomb(golomb(n - 1)))
```

Rewrite them as **`fib(n, memo)`** and **`golomb(n, memo)`**, where `memo` is a dict passed in by the caller (the tests call `fib(n, {})`). Before computing `n`, check whether it's already in `memo`; after computing it, store it there. Pass the **same** memo to every recursive call.

### Examples

```text
fib(10, {})       →  55
fib(100, {})      →  354224848179261915075
[golomb(n, {}) for n in range(1, 11)]   →  [1, 2, 2, 3, 3, 4, 4, 4, 5, 5]
```
