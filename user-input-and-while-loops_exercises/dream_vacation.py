# Dream vacation 7.10

poll = {}

# Setting a flag

poll_active = True

# Loop containing program

while poll_active:
    name = input("Enter your name: ")
    prompt = input("If you could visit one place in the world, where would you go? ")

    # Store responses in the dictionary
    poll [name] = prompt

    # Confirm no more people want to make entries
    repeat_poll = input("Would someone else like to take the poll? (yes or no) ")

    if repeat_poll == 'no':
        poll_active = False
    
# Print poll results
print("\n--- The results!!! ---")
for name, prompt in poll.items():
    print(f"{name} dreams of visitng {prompt}!")

