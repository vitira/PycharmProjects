#5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:
users = ["Lena", "Piter", "admin", "Marsha", "Nataly", "Daru"]
for user in users:
    print(f"Hi, {user.title()}. Good to see you again")###################??????????????????
print("")

#### If the username is 'admin', print a special greeting, such as Hello admin,
#would you like to see a status report?
#### Otherwise, print a generic greeting, such as Hello Eric, thank you for log-
# gin in again.
users = ["Lena", "Piter", "admin", "Marsha", "Nataly", "Daru"]
for user in users:
    if user == "admin":
        print(f"Hi {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for login in again")