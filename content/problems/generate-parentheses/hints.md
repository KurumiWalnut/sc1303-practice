Build the string one character at a time, keeping count of how many `(` and `)` you've used:

- You can add `(` while you've used fewer than `n`.
- You can add `)` only while it closes something: fewer `)` than `(` so far.
- When the string has length `2n`, record it.

This never builds an invalid string, so it's much faster than generating all 2²ⁿ strings and filtering.
