`City` (with `name` and a `routes` dict from `City` to price) is already loaded, with the helpers `build_cities`, `path_price` and the lecture's `LECTURE_ROUTES` (see **Provided code**).

Write `dijkstra_shortest_path(starting_city, final_destination)` from the course template. It returns `(cheapest_price, path)`, where `path` is the list of city **names** from start to destination.

Keep the two tables from the lecture, keyed by city name: `cheapest_prices_table` and `cheapest_previous_stopover_city_table`. Then repeat until no city is unvisited:

1. Mark the current city as visited and remove it from the unvisited list.
2. For each route out of it, add the neighbour to the unvisited list if it's new. If going through the current city is cheaper than the table's price (or the neighbour has no price yet), update both tables.
3. Make the **cheapest unvisited** city the current city.

Finally, walk back from the destination through the stopover table to build the path. You can assume the destination can be reached.

### Example (from the lecture)

```text
cities = build_cities(LECTURE_ROUTES)
dijkstra_shortest_path(cities["Atlanta"], cities["El Paso"])
    →  (280, ['Atlanta', 'Denver', 'Chicago', 'El Paso'])
```
