There are `n` locked rooms, numbered `0` to `n - 1`, except room 0, which is open. `rooms[i]` lists the keys you find in room `i`: each key opens the room with that number. Write `can_visit_all_rooms(rooms)` that returns `True` if you can get into **every** room.

### Examples

```text
can_visit_all_rooms([[1], [2], [3], []])              →  True
can_visit_all_rooms([[1, 3], [3, 0, 1], [2], [0]])    →  False   (the key to room 2 is inside room 2)
```

### Constraints

- `2 <= n <= 1000`; up to 3 000 keys in total.
- The rooms can form a chain 1 000 long, which is too deep for recursion in Python.
