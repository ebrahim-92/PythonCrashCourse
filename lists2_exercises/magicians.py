# Lists Chapter 5 practice exercises

# Using a for loop

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

# Doing more work in  a loop
    
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick {magician.title()}.\n")
print("Thank you everyone that was a great show!")