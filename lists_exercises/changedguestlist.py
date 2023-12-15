# Changing your guest list 3.5

guests = ["Saladin", "Alexander the Great", "Khalid Bin Walid"]
message = f"Mr. {guests[0]} you are cordially invited to dinner."
message1= f"Mr. {guests[1]} you are cordially invited to dinner."
message2 = f"Mr. {guests[2]} you are cordially invited to dinner."

print(message)
print(message1)
print(message2)

print(f"It appears Mr. {guests[1]} cannot make it")

guests.append("Genghis Khan")
message3 = f"My. {guests[3]} you are cordially invited to dinner."

print(message)
print(message3)
print(message2)