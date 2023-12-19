# Cities 8.5

def describe_city(city, country = "Iraq"):
    """Display city and country."""
    print(f"\nThe city {city.title()} is in {country.title()}")

describe_city("basrah")
describe_city("baghdad")
describe_city("doha", country = "qatar")