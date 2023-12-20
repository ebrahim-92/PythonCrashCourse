# Battery Upgrade 9.9

class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class Battery:
    """Initialize battery's attributes"""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print statement about battery size"""
        print(f"This car has a {self.battery_size}-kwh battery size")

    def get_range(self):
        """Range battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

    def upgrade_battery(self, battery_size):
        if self.battery_size < 100:
            battery_size == 100
        else:
            self.battery_size == 100
        
class ElectricCar(Car):
    """Car aspects specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize parent class attributes"""
        super().__init__(make, model, year)
        self.battery_size = Battery()

my_tesla = ElectricCar('tesla', 'model s', '2023')
print(my_tesla.descriptive_name())
my_tesla.battery.get_range()