A search box suggests products as you type. Write `suggested_products(products, search_word)`.

After each character of `search_word` is typed, suggest **at most 3** products that start with what has been typed so far. If more than 3 match, pick the 3 that come first **alphabetically**. Return a list with one list of suggestions per character typed.

### Examples

```text
suggested_products(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")
  →  [["mobile", "moneypot", "monitor"],
      ["mobile", "moneypot", "monitor"],
      ["mouse", "mousepad"],
      ["mouse", "mousepad"],
      ["mouse", "mousepad"]]

suggested_products(["havana"], "tatiana")  →  [[], [], [], [], [], [], []]
```

### Constraints

- Up to 50 000 distinct products; `search_word` has up to 20 000 letters.
