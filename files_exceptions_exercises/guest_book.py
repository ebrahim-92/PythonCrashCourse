# Guest book 10.4

file = "files_exceptions_exercises/guest.txt"

with open(file, "w") as guest_list:
    greet = input("Please enter your name: ")
    guest_list.write(greet)
    

    while greet:
        print(f"Welcome, {greet}!! \n")
        guest_list.write(f" visited website \n")
        break