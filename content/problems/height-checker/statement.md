Students should stand in **non-decreasing** order of height. `heights` is the order they're standing in now. Write `height_checker(heights)` that returns how many positions hold the **wrong** height, compared with the sorted order.

### Examples

```text
height_checker([1, 1, 4, 2, 1, 3])   →  3     sorted is [1, 1, 1, 2, 3, 4]
height_checker([5, 1, 2, 3, 4])      →  5
height_checker([1, 2, 3, 4, 5])      →  0
```

### Constraints

- Heights are between 1 and 100.
