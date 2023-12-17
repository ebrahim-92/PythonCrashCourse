# Rivers 6.5

rivers = {
    'egypt': 'Nile',
    'brazil': 'Amazon',
    'iraq': 'Euphrates',
}

# Task one, loop making statement about each river

for country, river in rivers.items():
    print(f"\nThe country {country.title()} contains the {river.title()} River")

# Task two, loop that prints name of each river
    
for river in rivers.values():
    print(river)

# Task three, loop that prints name of each country

for country in rivers.keys():
    print(country.title())