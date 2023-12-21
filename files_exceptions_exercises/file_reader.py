# Reading from a file practice

with open("files_exceptions_exercises/pi_digits.txt", "r") as file_object:
    contents = file_object.read()
    print(contents)

# Reading line by line practice
    
filename = "files_exceptions_exercises/pi_digits.txt"

with open(filename) as file_object2:
    for line in file_object2:
        print(line.rstrip())

# Making a list from file

with open(filename) as file_object3:
    lines = file_object3.readlines()

for line in lines:
    print(line.rstrip())