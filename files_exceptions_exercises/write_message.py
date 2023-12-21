# Writing to a file practice

filename = "files_exceptions_exercises/programming.txt"

with open(filename, "w") as file_object:
    file_object.write("I like programming. \n")
    file_object.write("I like creating videogames. \n")

# Appending to a file practice
    
with open(filename, "a") as file_object:
    file_object.write("I also like finding meaning in large datasets. \n")
    file_object.write("I like creating apps tha can run in a browser. \n")