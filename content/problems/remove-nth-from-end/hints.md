Can you do it in **one pass**?

---

Start a `fast` pointer `n` nodes ahead of a `slow` pointer, then move both until `fast` reaches the end. `slow` is then just before the node to remove. A dummy node in front of the head makes removing the head easy.
