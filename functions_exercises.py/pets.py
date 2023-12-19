# Passing different types of arguments to functions practice

# Positional arguments practice

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}")

describe_pet("cat", "mufasa")

# Keyword arguments practice

def describe_pet_modded(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}")

describe_pet_modded(animal_type= "dog", pet_name= "lassy")