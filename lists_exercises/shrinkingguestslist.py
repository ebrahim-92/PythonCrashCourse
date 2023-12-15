# Shrinking guests list 3.7

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

print("Greetings! We have found a larger dinner table and will invite more guests")

guests.insert(0, "Attila the Hun")
guests.insert(1, "Cyrus the Great")
guests.append("Napolean Bonaparte")

message4 = f"My. {guests[0]} you are cordially invited to dinner."
message5 = f"My. {guests[1]} you are cordially invited to dinner."
message6 = f"My. {guests[6]} you are cordially invited to dinner."

print(message4)
print(message5)
print(message6)

print("Apologies I just discovered I can only have two guests")

first_pop = guests.pop(0)
print(f"Apologies {first_pop} I regret to inform you that you are not invited")

second_pop = guests.pop(0)
print(f"Apologies {second_pop} I regret to inform you that you are not invited")

third_pop = guests.pop(1)
print(f"Apologies {third_pop} I regret to inform you that you are not invited")

fourth_pop = guests.pop(2)
print(f"Apologies {fourth_pop} I regret to inform you that you are not invited")

fifth_pop = guests.pop(2)
print(f"Apologies {fifth_pop} I regret to inform you that you are not invited")

print(f"Dear, {guests[0]} you are still invited!")
print(f"Dear, {guests[1]} you are still invited!")

del guests[0]
del guests[0]

print(guests)
