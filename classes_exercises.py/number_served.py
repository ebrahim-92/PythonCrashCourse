# Number Served 9.4

class Restaurant:
    """An attempt to model a restaurant"""
    def __init__(self, restaurant_name, restaurant_cuisine):
        self.restaurant_name = restaurant_name
        self.restaurant_cuisine = restaurant_cuisine
        self.number_served = 0

    def describe_restaurant(self):
        description = f"The restaurant is named {self.restaurant_name} and the restaurant's cuisine is {self.restaurant_cuisine}"
        return description

    def open_restaurant(self):
        print("The restaurant is open!")

    def number_serve(self):
        print(f"The restaurant served {self.number_serve} dishes")

    def set_number_serve(self,total_dishes):
        """Set a number of dishes served"""
        self.number_served = total_dishes

    def increment_number_serve(self,dishes):
        self.number_served += dishes



restaurant = Restaurant('PF Chang', 'Chinese')
restaurant.set_number_serve(5)
restaurant.number_serve()
restaurant.increment_number_serve(12)
restaurant.number_serve()