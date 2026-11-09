Write `daily_temperatures(temps)` that returns a list where `answer[i]` is how many days after day `i` you have to wait for a **warmer** day, or `0` if there's none.

### Examples

```text
daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])   →  [1, 1, 4, 2, 1, 1, 0, 0]
daily_temperatures([30, 40, 50, 60])                   →  [1, 1, 1, 0]
daily_temperatures([30, 60, 90])                       →  [1, 1, 0]
```

### Constraints

- Up to 100 000 days; temperatures between 30 and 100.
