Write `int_sqrt(n)` that returns the **integer part** of the square root of `n`: the largest whole number `r` with `r * r ≤ n`.

Don't use `math.sqrt`, `math.isqrt`, `** 0.5` or `pow`.

> [!PROF-NOTE] Week 6 seminar notebook
>
> The seminar's `integer_sqrt(x)` also counts its steps and returns `(answer, steps)`. Here, return just the answer. In the quiz, return whatever the question asks for.

### Examples

```text
int_sqrt(45)     →  6      (6 × 6 = 36 ≤ 45 < 49 = 7 × 7)
int_sqrt(99999)  →  316
int_sqrt(8)      →  2
```

### Constraints

- `0 ≤ n ≤ 2³¹ − 1`
- One hidden test calls your function 5 000 times with values around two billion.
