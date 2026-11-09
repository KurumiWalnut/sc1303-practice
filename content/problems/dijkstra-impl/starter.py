# City, build_cities, path_price and LECTURE_ROUTES are already loaded.


def dijkstra_shortest_path(starting_city, final_destination):
    cheapest_prices_table = {}
    cheapest_previous_stopover_city_table = {}
    unvisited_cities = [starting_city]
    visited_cities = {}

    cheapest_prices_table[starting_city.name] = 0
    current_city = starting_city

    while unvisited_cities:
        # TODO 1: mark current_city as visited and remove it from unvisited_cities
        # TODO 2: look at every route out of current_city and update the tables
        # TODO 3: make the cheapest unvisited city the new current_city
        break  # TODO: delete this line once the loop body is written

    cheapest_price = cheapest_prices_table[final_destination.name]
    shortest_path = []
    current_city_name = final_destination.name
    while current_city_name:
        shortest_path.insert(0, current_city_name)
        current_city_name = cheapest_previous_stopover_city_table.get(current_city_name)
    return cheapest_price, shortest_path
