The answer is the largest number of intervals covering any one point (think "meeting rooms needed").

---

- **Sort** the starts and, separately, the ends.
- Sweep through the starts in order. Before counting a start, release every interval that **ended before** it (`end < start`, because ends are inclusive). Track the most intervals open at once.

Or: sort by start and keep a min-heap of group end times. Reuse the earliest-ending group if it ended before this start; otherwise open a new one.
