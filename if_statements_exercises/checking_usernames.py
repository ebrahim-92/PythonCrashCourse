# Checking usernames 5.10

current_users = ["kratos", "altair", "drake", "dragonborn", "geralt"]
new_users = ["geralt", "dragonborn", "ezio", "prince", "slender man"]

for users in new_users:
    
    if users in current_users:
        print("The username is unavailable please try a new one.")
    else:
        print("That username is available")