Sorting by value doesn't work (`9` should come before `34`), and neither does sorting the digits as strings (`3` should come before `30`, since `330 > 303`).

---

The right order between two numbers `a` and `b` (as strings) is: `a` first if `a + b > b + a`. Sort with that comparison using `functools.cmp_to_key`, then join.
