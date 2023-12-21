# Guest 10.3

file = "files_exceptions_exercises/guest.txt"

with open(file, "w") as guest_list:
    greet = input("Please enter your name: ")
    guest_list.write(greet)