## The problem

In a **weighted** graph, find the cheapest route from a start vertex to the others. BFS finds the fewest **edges**, but the fewest edges isn't always the lowest total **price**.

The course stores cities like this (`dijkstra_template.py`):

```python
class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}             # City -> price

    def add_route(self, city, price):
        self.routes[city] = price
```

## Dijkstra's algorithm (the course version)

Keep two tables, keyed by city name:

- `cheapest_prices_table[name]`: the cheapest price found **so far** from the start to that city.
- `cheapest_previous_stopover_city_table[name]`: the city you came from on that cheapest route.

Then:

1. Start at the starting city, with price 0.
2. **Visit** the current city: mark it visited and remove it from the unvisited list.
3. For each route out of it: the price through here = `prices[current] + route price`. If that's cheaper than what's in the table (or the city isn't in the table yet), update both tables. Add the city to the unvisited list if it's new.
4. The next current city is the **unvisited city with the lowest price** in the table.
5. Repeat until nothing is unvisited.

```python
for adjacent, price in current_city.routes.items():
    if adjacent.name not in visited_cities and adjacent not in unvisited_cities:
        unvisited_cities.append(adjacent)
    price_through_current = cheapest_prices_table[current_city.name] + price
    if adjacent.name not in cheapest_prices_table or price_through_current < cheapest_prices_table[adjacent.name]:
        cheapest_prices_table[adjacent.name] = price_through_current
        cheapest_previous_stopover_city_table[adjacent.name] = current_city.name
```

> [!PROF-BUG] Week 12 seminar solution, dijkstra.py
>
> It checks `if not cheapest_prices_table.get(adjacent_city.name) or ...` to mean "no price yet". But the starting city's price is `0`, and `not 0` is `True`. So when a route leads **back to the start**, the start gets a new price and a stopover, and rebuilding the path then goes round in a circle forever. With the lecture's cities, starting from Boston never finishes, because `El Paso → Boston` leads back. The Atlanta example only works because no route goes back to Atlanta.
>
> Check whether the key is in the table instead:
>
> ```python
> if adjacent_city.name not in cheapest_prices_table or ...:
> ```

## Rebuilding the path

Walk **backwards** from the destination through the stopover table until you reach the start, then reverse:

```text
El Paso ← Chicago ← Denver ← Atlanta     →   ['Atlanta', 'Denver', 'Chicago', 'El Paso'], price 280
```

## Why it works, and when it doesn't

The cheapest unvisited city can't get any cheaper later, because every other route to it costs at least as much **as long as no price is negative**. With negative weights, Dijkstra can give wrong answers.

## How fast?

| Version | Picking the next city | Total |
|---|---|---|
| Course version (scan the unvisited list) | O(V) each time | **O(V²)** |
| With a heap (`heapq`) | O(log V) | **O((V + E) log V)** |

The heap version, the one you'll write for LeetCode-style questions:

```python
import heapq

def dijkstra(adj, start):                   # adj[u] = [(v, weight), ...]
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue                        # an old, out-of-date entry: skip it
        for v, w in adj[u]:
            if d + w < dist.get(v, float("inf")):
                dist[v] = d + w
                heapq.heappush(heap, (d + w, v))
    return dist
```

## Variations

| Question | Change |
|---|---|
| Highest **probability** path | multiply instead of add; always take the **largest** next (push negatives) |
| Path whose **biggest** step is smallest | cost of a path = `max(cost so far, edge)` instead of `+` |
| Cheapest with **at most k stops** | the plain algorithm can throw away a pricier route that uses fewer stops; do k + 1 rounds of edge relaxation (Bellman-Ford) instead |

## Common bugs

- Picking the next city as the **closest neighbour** instead of the cheapest **unvisited city overall**.
- Updating a city that's already visited.
- Writing `if not cheapest_prices_table.get(name)` to mean "no price yet". The start's price is 0, which counts as false too (see the box above).
- Looking up `visited_cities` by `City` object when it's keyed by name, so no city ever counts as visited.
- Forgetting the stopover table, so you can't rebuild the path.
- With a heap: not skipping the out-of-date entries, which wastes time (not wrong, but slow).
