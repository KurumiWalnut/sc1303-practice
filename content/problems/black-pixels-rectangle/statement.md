`image` is a grid (a list of rows) of `"0"` (white) and `"1"` (black) pixels. The black pixels form **one connected region**: you can walk between any two of them by moving up, down, left or right. `(x, y)` is one black pixel, where `x` is the **row** and `y` the **column**.

Write `min_area(image, x, y)` that returns the area of the **smallest rectangle**, with sides along the grid, that contains every black pixel.

Checking every pixel works, but it's slow. Use the black pixel you're given to binary search instead (see the hints). The seminar version also returned step counters; here, return just the area.

### Example (seminar)

```text
image = [["0", "0", "1", "0"],
         ["0", "1", "1", "0"],
         ["0", "1", "0", "0"]]
min_area(image, 0, 2)   →  6      rows 0 to 2, columns 1 to 2: 3 × 2
```

### Constraints

- `1 <= len(image), len(image[0]) <= 1500`
- One hidden test asks 40 questions about a 1 500 × 1 500 image with over a million black pixels, so checking every pixel, or visiting every black pixel, runs out of time.
