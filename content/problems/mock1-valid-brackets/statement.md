Write `is_valid(s)`. The string `s` contains only the characters `( ) [ ] { }`. Return `True` if the brackets are balanced and `False` otherwise.

The brackets are balanced when:

- every opening bracket is closed by the **same type** of bracket, and
- brackets are closed in the **correct order** (the most recently opened one closes first).

An empty string is balanced.

### Examples

```text
is_valid("()")       →  True
is_valid("()[]{}")   →  True
is_valid("(]")       →  False
is_valid("([)]")     →  False
is_valid("{[()]}")   →  True
```

### Constraints

- `0 ≤ len(s) ≤ 102 000`
