def find_cheapest_price(n, flights, src, dst, k):
    INF = float("inf")
    price = [INF] * n
    price[src] = 0
    for _ in range(k + 1):                         # one more flight per round
        new_price = price[:]                       # relax from the OLD prices only
        for a, b, cost in flights:
            if price[a] + cost < new_price[b]:
                new_price[b] = price[a] + cost
        price = new_price
    return price[dst] if price[dst] != INF else -1
