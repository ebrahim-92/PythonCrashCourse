# Learning Python 10.1

file = "files_exceptions_exercises/learning_python.txt"

with open(file) as file_object:
    contents = file_object.read()
    print(contents)