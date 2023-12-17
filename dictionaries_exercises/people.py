# People 6.7

person = {
    'first_name': 'Mike',
    'last_name': 'Jones',
    'age': 36,
    'city': 'Houston',
}

person2 = {
    'first_name': 'Spike',
    'last_name': 'Dudley',
    'age': 50,
    'city': 'Chicago',    
}

person3 = {
    'first_name': 'Leon',
    'last_name': 'Scott',
    'age': 32,
    'city': 'London',
}

people = [person, person2, person3]

for person in people:
    print(f"\n{person['first_name']} {person['last_name']} {person['age']} {person['city']}")
