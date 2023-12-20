# Users 9.3

class User:
    """A simple attempt to represent users"""
    def __init__(self,first_name,last_name,age,email):
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"\nThe user's name is {self.firstname.title()} {self.lastname.title()} they are {self.age} year's old and their email is {self.email}")
    
    def greet_user(self):
        print(f"\nHello, {self.firstname.title()} thank you for coming!")

user1 = User('mohammed','salah',28,'mo.salah@gmail')
user2 = User('cristiano','ronaldo',35,'cr7@gmail.com')
user3 = User('zlatan','ibrahimovic',38,'zlatan@gmail.com')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
