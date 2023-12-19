# Passing lists to functions practice

def greet_users(names):
    """Display greeting for each user in list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)