class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_route(self, city, price):
        self.routes[city] = price


def build_cities(routes):
    """{"Atlanta": {"Boston": 100, ...}, ...} -> {name: City}, adding routes in the order listed."""
    cities = {}
    for name, outs in routes.items():
        for n in [name, *outs]:
            if n not in cities:
                cities[n] = City(n)
    for name, outs in routes.items():
        for other, price in outs.items():
            cities[name].add_route(cities[other], price)
    return cities


def path_price(cities, path):
    """The total price of following path (a list of city names), or None if a hop has no route."""
    total = 0
    for a, b in zip(path, path[1:]):
        if cities[b] not in cities[a].routes:
            return None
        total += cities[a].routes[cities[b]]
    return total


LECTURE_ROUTES = {
    "Atlanta": {"Boston": 100, "Denver": 160},
    "Boston": {"Chicago": 120, "Denver": 180},
    "Chicago": {"El Paso": 80},
    "Denver": {"Chicago": 40, "El Paso": 140},
    "El Paso": {"Boston": 100},
}
