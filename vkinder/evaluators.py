def evaluate_city(city, my_city, cost=10):
    match = 10
    if city == my_city:
        return match * cost
    else:
        return 0


def city_to_string(city: dict) -> str:
    return city['title']


def dummy(anything):
    return anything
