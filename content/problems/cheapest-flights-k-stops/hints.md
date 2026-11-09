Plain Dijkstra can go wrong here: it keeps only the cheapest price to each city, but a pricier route with **fewer** stops might be the only one that still has stops to spare.

---

Use **k + 1 rounds of Bellman-Ford** instead. Keep `price[city]`. In each round, start from a **copy** of the previous round's prices and relax every flight from the old prices. After round `i`, `price` holds the cheapest routes with at most `i` flights.
