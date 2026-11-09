Go through the tokens with a stack:

- A number: push it (as an `int`).
- An operator `+ - * /`: pop **b** (the right operand) **first**, then **a**, and push `a op b`.

---

Python's `//` rounds down (`7 // -2` is `-4`), so use `int(a / b)`.
