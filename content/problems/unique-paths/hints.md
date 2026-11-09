The number of paths to a cell is the paths to the cell **above** it plus the paths to the cell on its **left**.

---

Every cell in the top row or left column has exactly 1 path. Memoize on `(row, col)`, or fill a table row by row.
