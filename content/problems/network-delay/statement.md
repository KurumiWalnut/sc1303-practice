A network has `n` nodes, labelled `1` to `n`. `times[i] = [u, v, w]` means a signal takes `w` time to travel from `u` to `v` (one way). A signal is sent from node `k`. Write `network_delay_time(times, n, k)` that returns how long it takes for **every** node to receive it, or `-1` if some node never does.

### Examples

```text
network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)   →  2
network_delay_time([[1, 2, 1]], 2, 1)                         →  1
network_delay_time([[1, 2, 1]], 2, 2)                         →  -1
```

### Constraints

- `1 <= n <= 2000`; up to 20 000 edges; `0 <= w <= 100`.
