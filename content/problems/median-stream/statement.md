The tests drive your class through `run_ops` (see **Provided code**).

Write a class `MedianFinder` with:

- **`add_num(num)`**: add a number to the collection.
- **`find_median()`**: return the median of every number added so far, as a float. With an even count, it's the average of the two middle values.

### Example

```text
add_num(1), add_num(2)
find_median()   →  1.5
add_num(3)
find_median()   →  2.0
```

### Constraints

- Up to 100 000 calls to `add_num` and 50 000 to `find_median`; `find_median` is only called after at least one number has been added.
