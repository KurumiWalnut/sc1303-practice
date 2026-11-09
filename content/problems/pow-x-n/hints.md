Multiplying `x` by itself `n` times is far too slow when `n` is about 2 billion. Halve the problem instead.

---

- xⁿ = (x^(n/2))² when `n` is even,
- xⁿ = x · (x^((n-1)/2))² when `n` is odd,
- x⁻ⁿ = 1 / xⁿ.

Compute x^(n/2) **once** and square it, rather than calling the function twice. That's only about 31 levels of recursion.
