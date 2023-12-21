# Favorite Number 10.11

import json

favorite_number = input("What is your favorite number? ")
favorite_number_list = 'favorite_number.json'

with open(favorite_number_list, 'w') as f:
    json.dump(favorite_number, f)

