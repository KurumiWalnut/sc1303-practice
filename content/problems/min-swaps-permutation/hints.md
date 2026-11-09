Selection sort (swapping only when needed) happens to use the minimum number of swaps here, but it's O(N²). Think in **cycles** instead: value `v` belongs at index `v`.

---

Start at any index, jump to the index where its value belongs, and keep going until you're back where you started. That's one cycle. A cycle of length `L` needs `L - 1` swaps, so the answer is `n - (number of cycles)`. O(N).
