Write `product_except_self(nums)` that returns a list where `answer[i]` is the product of every value in `nums` **except** `nums[i]`. Don't use division (it breaks when there's a 0 anyway).

### Examples

```text
product_except_self([1, 2, 3, 4])         →  [24, 12, 8, 6]
product_except_self([-1, 1, 0, -3, 3])    →  [0, 0, 9, 0, 0]
```

### Constraints

- `2 <= len(nums) <= 100 000`; every product fits in a 32-bit integer.
