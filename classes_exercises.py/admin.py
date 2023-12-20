# Admin 9.7

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

class Admin(User):
    """Admin class"""
    def __init__(self,first_name,last_name,age,email):
        super().__init__(first_name,last_name,age,email)
        self.privileges = ['can add post', 'can ban user']
    
    def show_privileges(self):
        print(self.privileges)

privileges = Admin("john", "smith", 50, "jsmith@gmail.com")
privileges.show_privileges()