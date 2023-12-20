# Three restaurants 9.2

class Restaurant:
    """An attempt to model a restaurant"""
    def __init__(self,restaurant_name,restaurant_cuisine):
        self.restaurant_name = restaurant_name
        self.restaurant_cuisine = restaurant_cuisine

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name}")
        print(f"The restaurant's cuisine is {self.restaurant_cuisine}")

    def open_restaurant(self):
        print("The restaurant is open!")

# Creating three instances

restaurant1 = Restaurant('PF Chang', 'Chinese')
restaurant2 = Restaurant('Al Shami', 'Arabic')
restaurant3 = Restaurant('KFC', 'fast food')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()