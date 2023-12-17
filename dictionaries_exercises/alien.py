# Dictionaries Practice

alien_0 = {"color" : "green", "points" : "5"}
print(alien_0["color"])
print(alien_0["points"])

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")

# Adding new key-value pairs to a dictionary

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# Starting with an empty dictionary and adding to it

alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

# Modifying values in a dictionary

alien_0 = {"color" : "green"}
print(f"This alien is of the color {alien_0['color']}.")
alien_0["color"] = "yellow"
print(f"This alien is of the color {alien_0['color']}.")


# Position alien can move at different speeds

alien_0 = {"x-position" : 0, "y-position" : 25, "speed" : "medium"}
print(f"Original position: {alien_0['x-position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus the increment
alien_0["x-position"] = alien_0["x-position"] + x_increment

print(f"New position: {alien_0['x-position']}")

# Removing a key-value pair

del alien_0["speed"]
print(alien_0)