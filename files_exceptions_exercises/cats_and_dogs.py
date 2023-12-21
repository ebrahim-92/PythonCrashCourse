# Cats and dogs 10.8

cat_file = "files_exceptions_exercises/cats.txt"
dog_file = "files_exceptions_exercises/dogs.txt"

try:
    with open(cat_file) as cat_object:
        cat_list = cat_object.read()
    with open(dog_file) as dog_object:
        dog_list = dog_object.read()
except FileNotFoundError:
    print("File is missing!")
else:
    print(cat_list)
    print(dog_list)