# Practice exercises of putting squared values into a list

# First method for squaring the numbers in a range

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
    print(squares)

# Shorter method for writing this program by removing temporary variable

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

# Using list comprehensions to shorten the code further

squares = [value ** 2 for value in range(1,11)]
print(squares)