Keep a stack of the **indexes of days still waiting** for a warmer day.

---

Their temperatures never increase from bottom to top. For each new day, pop every waiting day that's colder than it and fill in its answer (`today - that_day`), then push today. Each day is pushed and popped once: O(N).

Looking ahead from every day is O(N²) when temperatures keep falling.
