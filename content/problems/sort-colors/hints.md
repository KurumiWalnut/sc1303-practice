Use the **Dutch national flag** partition, with three pointers.

---

Keep three pointers:

- `low`: everything before it is 0,
- `high`: everything after it is 2,
- `mid`: scans the unknown part between them.

Look at `nums[mid]`. If it's 0, swap it to `low` and move both `low` and `mid` on. If it's 2, swap it to `high` and move `high` back (don't move `mid`: the value swapped in hasn't been checked yet). If it's 1, just move `mid` on.
