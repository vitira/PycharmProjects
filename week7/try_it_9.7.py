# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

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

class Admin(User):
    def __init__(self,first_name, last_name, age, position, company, privileges):
        self.privileges = privileges
        super().__init__(first_name, last_name, age, position, company)

    def show_privileges(self):
        print(f"Privilages: {self.privileges}")


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

privileges = Admin("Ivan", "Petrov", 30, "menager", "Best Design", ["can add post", "can delete post",
                                                                           "can ban user"])

privileges.show_privileges()

