# Testing function practice continued

from name_function import get_formatted_name

print("Enter 'q' to quit at any time")
while True:
    first = input("\nEnter a first name: ")
    if first == 'q':
        break
    last = input("\nEnter a last name: ")
    if last == 'q':
        break

formatted_name = get_formatted_name(first, last)
print(f"\tNeatly formatted name: {formatted_name}")