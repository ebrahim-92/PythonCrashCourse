# Login Attempts 9.5

class User:
    """A simple attempt to represent users"""
    def __init__(self,first_name,last_name,age,email):
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        user = f"{self.firstname} {self.lastname} {self.age} {self.email}"
        return user
    
    def greet_user(self):
        print(f"\nHello, {self.firstname.title()} thank you for coming!")
    
    def increment_login_attempts(self,logins):
        """Increment login attempts"""
        self.login_attempts += logins

    def reset_login_attempts(self, reset):
        """Reset login attempts"""
        self.login_attempts = 0

user1 = User('mohammed','salah',28,'mo.salah@gmail')
print(user1.describe_user().title())
user1.increment_login_attempts(5)
print(user1.increment_login_attempts)
