# 4.11 My Pizzas, Your Pizzas: Start with your program from exercise 4.1(page 60). Make a copy of the list of pizzas,
# and call it friend pizzas. Then do following:
pizzas = ["cheese", "pepperoni", "doublecheese"]
friend_pizzas = pizzas [ : ]
print(pizzas)
print(friend_pizzas)
print('###########################')
#### Add a new pizza to the original list
pizzas.append("triplecheese")
print(pizzas)

####Add a different pizza to the list friend_pizzas.
friend_pizzas.append("sousage")
print(friend_pizzas)

####Prove that you have two separate lists. Print the message, My favorite
#pizzas are:, and then use a for loop to print the first list. Print the message,
#My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is
# stored in the appropriate list.
for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza}")
print("################")
for friend_pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are: {friend_pizza}")