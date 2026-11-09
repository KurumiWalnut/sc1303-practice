Two good approaches:

- **Trie:** insert the products in sorted order and keep the first 3 words that pass through each node.
- **Sort + binary search:** sort the products, and for each prefix use `bisect_left` to find where it would go; the next 3 products are the only candidates.
