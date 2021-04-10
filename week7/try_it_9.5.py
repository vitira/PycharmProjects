# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.

# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

class User():
    def __init__(self, first_name, last_name, age, position, company):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position
        self.company = company
        self.login_attempt = 0

    def increment_login_attempt(self):
        """Increment value of login attempt by one"""
        self.login_attempt += 1

    def reset_login_attempt(self):
        """Reset value of login attempt to zero"""
        self.login_attempt = 0




    def describe_user(self):
        print(f"User {self.first_name} {self.last_name}, age: {self.age}, position in company: {self.position}, "
              f"company name: {self.company}")

    def great_user(self):
        print(f"Hello {self.first_name}")

user1 = User("Ivan", "Petrov", 30, "menager", "Best Design")
user1.describe_user()
user1.great_user()
print("==================")

user2 = User("Villiam", "Pak", 70, "company owner", "Best Cotton")
user2.describe_user()
user2.great_user()
print("==================")

user3 = User("Evgeny", "Govtonog", 30, "senior software engineer", "Israel communication")
user3.describe_user()
user3.great_user()

user3.increment_login_attempt()
print(f"user3 increment {user3.login_attempt}")
user3.increment_login_attempt()
print(f"user3 increment {user3.login_attempt}")
user3.increment_login_attempt()
print(f"user3 increment {user3.login_attempt}")

user3.reset_login_attempt()
print(f"Reset login attempt {user3.login_attempt}")