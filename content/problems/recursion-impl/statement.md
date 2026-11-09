Write each function **recursively** (no loops):

- **`sum_range(low, high)`**: the sum of every whole number from `low` to `high`, inclusive. If `low > high` the range is empty, so return 0.
- **`double_array(array, index=0)`**: double every number in `array` **in place**, starting at `index`. Return nothing.
- **`index_of_x(string)`**: the first index of `"x"` in `string`. The string always contains an `"x"`.
- **`add_until_100(array)`**: add the numbers from **right to left**, starting from the last one. Skip any number that would push the running total above 100. Make only **one** recursive call per level (the version in the exercise makes two, which is O(2ᴺ)).

### Examples

```text
sum_range(1, 10)                  →  55
a = [1, 2, 3]; double_array(a)    →  a is [2, 4, 6]
index_of_x("abcdefghijklmnopqrstuvwxyz")   →  23
add_until_100([30, 50, 40, 20])   →  90    (20, then 40 → 60, 50 would make 110 so skip it, then 30 → 90)
```
