Write these four functions **without** `list.insert`, `list.remove`, `list.index`, `reverse()` or slicing tricks. Do the work with loops, so you can count the steps.

- **`linear_search(arr, target)`**: return `(index, steps)`, where `steps` is how many elements you compared. If `target` isn't there, return `(-1, steps)`.
- **`insert_at(arr, index, value)`**: insert `value` at `index` **in place**, shifting later elements one place right. Return the number of **shifts**. (`arr.append(None)` to make room is fine.)
- **`delete_by_value(arr, value)`**: remove the **first** occurrence of `value` in place by shifting the later elements one place left, then drop the last slot (`arr.pop()` is fine). Return the number of **shifts**, or the string `"Value not found"`.
- **`reverse_array(arr)`**: reverse `arr` in place by swapping from both ends. Return the number of **swaps**.

### Examples

```text
linear_search([10, 20, 30, 40, 50], 30)   →  (2, 3)
a = [10, 20, 30, 40]; insert_at(a, 1, 15)        →  3,  a is [10, 15, 20, 30, 40]
a = [10, 20, 30, 20, 40]; delete_by_value(a, 20)  →  3,  a is [10, 30, 20, 40]
a = [1, 2, 3, 4, 5]; reverse_array(a)             →  2,  a is [5, 4, 3, 2, 1]
```
