Write a `Queue` class:

- **`enqueue(value)`**: add to the **back**.
- **`dequeue()`**: remove and return the **front** value, or `None` if the queue is empty.
- **`read()`**: return the front value without removing it, or `None` if empty.
- **`is_empty()`** and **`__len__()`**.

`dequeue` must be **O(1)**. `list.pop(0)` shifts every remaining item, so it's O(N) and too slow for the big test. Use `collections.deque` and `popleft()`.

### Example

```text
q = Queue()
q.enqueue("a"); q.enqueue("b"); q.enqueue("c")
q.read()       →  'a'
q.dequeue()    →  'a'
q.dequeue()    →  'b'
len(q)         →  1
```
