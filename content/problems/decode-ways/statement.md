Letters are encoded as numbers: `"A"` → `"1"`, `"B"` → `"2"`, …, `"Z"` → `"26"`. Write `num_decodings(s)` that returns how many ways the digit string `s` can be decoded back into letters.

A code can't start with `0`, so `"06"` isn't valid, but `"6"` is.

### Examples

```text
num_decodings("12")    →  2     ("AB" or "L")
num_decodings("226")   →  3     ("BZ", "VF", "BBF")
num_decodings("06")    →  0
```

### Constraints

- `1 <= len(s) <= 100`
