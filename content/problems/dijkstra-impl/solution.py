def dijkstra_shortest_path(starting_city, final_destination):
    cheapest_prices_table = {}
    cheapest_previous_stopover_city_table = {}
    unvisited_cities = [starting_city]
    visited_cities = {}

    cheapest_prices_table[starting_city.name] = 0
    current_city = starting_city

    while unvisited_cities:
        visited_cities[current_city.name] = True
        unvisited_cities.remove(current_city)

        for adjacent_city, price in current_city.routes.items():
            if adjacent_city.name not in visited_cities and adjacent_city not in unvisited_cities:
                unvisited_cities.append(adjacent_city)
            price_through_current_city = cheapest_prices_table[current_city.name] + price
            if (adjacent_city.name not in cheapest_prices_table
                    or price_through_current_city < cheapest_prices_table[adjacent_city.name]):
                cheapest_prices_table[adjacent_city.name] = price_through_current_city
                cheapest_previous_stopover_city_table[adjacent_city.name] = current_city.name

        if unvisited_cities:                      # the cheapest unvisited city is next
            current_city = min(unvisited_cities, key=lambda city: cheapest_prices_table[city.name])

    cheapest_price = cheapest_prices_table[final_destination.name]
    shortest_path = []
    current_city_name = final_destination.name
    while current_city_name:
        shortest_path.insert(0, current_city_name)
        current_city_name = cheapest_previous_stopover_city_table.get(current_city_name)
    return cheapest_price, shortest_path
