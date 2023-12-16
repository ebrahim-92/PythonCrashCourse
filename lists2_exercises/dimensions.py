# Working with tuples

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping through tuple

for dimension in dimensions:
    print(dimension)

# Writing over a tuple
dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimesions: ")
for dimension in dimensions:
    print(dimension)   