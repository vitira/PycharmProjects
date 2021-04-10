# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

class User():
    def __init__(self, first_name, last_name, age, position, company):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.position = position
        self.company = company

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

