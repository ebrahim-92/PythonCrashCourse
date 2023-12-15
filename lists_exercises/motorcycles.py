# Chapter practice exercises

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'

print(motorcycles)

# Adding more entries to lists

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# Appending to empty lists

cars = []
cars.append('toyota')
cars.append('bmw')
cars.append('mercedes')
print(cars)

# Using insert method to add to lists

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "ducati")
print(motorcycles)

# Removing items from lists

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)