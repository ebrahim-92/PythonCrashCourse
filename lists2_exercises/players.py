# Working with parts of lists practice

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

# Looping through a slice

players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are the players on my team:")
for player in players[:3]:
    print(player.title())