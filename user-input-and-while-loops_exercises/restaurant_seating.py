# Restaurant seating 7.2

seating = input("How many people are in your dinner group? ")
seating = int(seating)

# Conditionals on amount of people

if seating >= 8:
    print("You will have to wait for a table")
else:
    print("You do not have to wait for a table")