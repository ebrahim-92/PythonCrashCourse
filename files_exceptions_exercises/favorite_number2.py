# Favorite Number 10.11 part 2

import json

favorite_number_list = 'favorite_number.json'

with open(favorite_number_list) as f:
    favorite_number = json.load(f)
    print("Your favorite number is {favorite_number}")