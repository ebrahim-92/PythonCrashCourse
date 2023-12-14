#String exercises

#Using title method

name = "ada lovelace"
print(name.title())

#Using upper and lower method

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

#Splitting name into two variables

first_name = "Ada"
last_name = "Lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"

print(message)

#Adding and removing whitespace

print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

favorite_language = " python "
print(favorite_language)

print(favorite_language.rstrip())
print(favorite_language.lstrip())