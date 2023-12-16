# Hello admin 5.8

usernames = ["kratos", "admin", "altair", "dragonborn", "geralt"]

for username in usernames:
    if username == "admin":
        print(f"Hello {username.lower()}, would you like to see a status report?")
    else:
        print(f"Hello {username.title()} thanks for logging in today!")
