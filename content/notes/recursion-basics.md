## Two parts of every recursive function

1. **Base case**: the smallest input, answered directly without recursing.
2. **Recursive case**: solve a **smaller** version of the same problem, then build the answer from it.

```python
def factorial(n):
    if n <= 1:                 # base case
        return 1
    return n * factorial(n - 1)   # smaller problem
```

With no base case (or one that's never reached), the calls go on until Python stops them with `RecursionError: maximum recursion depth exceeded`. That's a **stack overflow**.

## The call stack

Each call is pushed onto the **call stack** and waits there until the call it made returns. `factorial(3)` pushes `factorial(3)`, `factorial(2)` and `factorial(1)`. Then they return in reverse order: 1, then 2 × 1, then 3 × 2.

Python allows about **1000** frames. A recursion that goes N levels deep fails for large N, even when the logic is right. In those cases, use a loop.

## Course exercises (Week 9)

**Sum from low to high:** the base case is `low == high`, or `low > high` for an empty range.

```python
def sum_range(low, high):
    if low > high:
        return 0
    return low + sum_range(low + 1, high)
```

**Double every element in place:** pass the index along.

```python
def double_array(array, index=0):
    if index >= len(array):
        return
    array[index] *= 2
    double_array(array, index + 1)
```

**First index of "x":** check the first character, then recurse on the rest and add 1.

```python
def index_of_x(string):
    if string[0] == "x":
        return 0
    return 1 + index_of_x(string[1:])
```

## Don't make the same call twice

```python
def add_until_100(array):              # slow: up to two recursive calls per level
    if not array:
        return 0
    if array[0] + add_until_100(array[1:]) > 100:
        return add_until_100(array[1:])
    return array[0] + add_until_100(array[1:])
```

Calling `add_until_100(array[1:])` twice **doubles** the work at every level: O(2ᴺ). Call it once, store the result in a variable and reuse it: O(N).

## Recursion for "choose or skip" problems

Many questions (all subsets, all valid bracket strings) are a tree of choices. At each step, try each option, recurse, then undo the choice. This is **backtracking**.

```python
def subsets(nums):
    out, chosen = [], []
    def go(i):
        if i == len(nums):
            out.append(chosen[:])      # copy, because chosen keeps changing
            return
        go(i + 1)                      # skip nums[i]
        chosen.append(nums[i])         # take nums[i]
        go(i + 1)
        chosen.pop()                   # undo
    go(0)
    return out
```

## Divide and conquer

To compute xⁿ, use x^(n/2) × x^(n/2), so the problem **halves** each time: O(log n) calls instead of n multiplications. Binary search and quicksort use the same idea.
