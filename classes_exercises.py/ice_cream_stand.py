# Ice Cream Stand 9.6

class Restaurant:
    """An attempt to model a restaurant"""
    def __init__(self,restaurant_name,restaurant_cuisine):
        self.restaurant_name = restaurant_name
        self.restaurant_cuisine = restaurant_cuisine
    

class IceCreamStand(Restaurant):
    """An attempt to model an ice cream stand"""
    def flavors(self, restaurant_name,restaurant_cuisine):
        super().__init__(restaurant_name,restaurant_cuisine)
        self.flavor = "vanilla, chocalate, strawberry"

    def display_flavors(self):
        print(f"The {self.restaurant_name} serves {self.restaurant_cuisine} which has {self.flavor}")

restaurant1 = IceCreamStand('dairy queen', 'ice cream')
restaurant1.display_flavors()