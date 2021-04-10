#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
#not empty.
#### If the list is empty, print the message We need to find some users!
#### Remove all of the usernames from your list, and make sure the correct
# message is printed.
#users = ["Lena", "Piter", "admin", "Marsha", "Nataly", "Daru"]
users = []
if users:
    for user in users:
        if user == "admin":
            print(f"Hi {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for login in again")
else:
    print("List is empty. We need to find some users")