Build a sorted list one node at a time. A **dummy** node in front of it saves special cases. For each node taken from the input, walk the sorted list from the dummy to find the last node with `data <=` the new one, and splice the new node in after it.

---

Inserting is O(1) once you've found the spot, but finding it from the front every time makes **already sorted** input O(N²). Remember the **last** node of the sorted list: if the new value is at least as big, just attach it there.
