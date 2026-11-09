Use Dijkstra on the grid, where the "distance" of a route is its biggest step so far.

---

Going from a cell with effort `e` across a step of size `s` costs `max(e, s)`. Pop the cell with the **smallest** effort from the heap. The first time you pop the target, you have the answer.
