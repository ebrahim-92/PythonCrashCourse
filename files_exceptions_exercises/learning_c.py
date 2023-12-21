# Learning C 10.2

file = "files_exceptions_exercises/learning_python.txt"

with open(file) as file_object:
    for line in file_object:
        line = line.replace('Python', 'Java')
        print(line)
