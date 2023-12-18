# Multiples of ten 7.3

number = input("Please enter a number and I will tell you if it is a multiple of ten: ")
number = int(number)

# Conditional statements to identify if number is a multiple of ten or not

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of ten")
else:
    print(f"\nThe number {number} is not a multiple of ten")