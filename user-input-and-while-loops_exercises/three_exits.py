# Three exits 7.6, same as movie_tickets program

prompt = input("\nPlease enter your age: ")
prompt = int(prompt)

# Loop to give different prices for different ages

while prompt:
    if prompt <= 3:
        print(f"\nYou are {prompt} your admission is free!")
    elif prompt <= 12:
        print(f"\nYou are {prompt} your admission is $10")
    else:
        print(f"\nYou are {prompt} your admission is $15")
    break