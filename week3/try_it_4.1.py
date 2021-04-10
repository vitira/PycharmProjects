#4.1 Pizzas: Think of at least three kinds of your favorite pizza. Store this pizza names in a list, and than use a
# for loop to print the name for each pizza.
pizzas = ["cheese", "pepperoni", "doublecheese"]
for pizza in pizzas:
    print(pizza.title())
print("")

#### Modify your for loop to print a sentence using the name of the pizza instead of printing just name of the pizza.
# For each pizza you should have one line of output containing a simple statement like "I like pepperoni pizza".
pizzas = ["cheese", "pepperoni", "doublecheese"]
for pizzza in pizzas:
    print("I like " + pizza + " pizza.")
print("\n")

#### Add a line at the and of your program, outside of for loop, that states how much you like pizza. The output should
# consist of tree or more lines about the kinds of pizza you like and then additional sentence, such as "I really like
# pizza!"
pizzas =("cheese", "pepperoni", "doublecheese")
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
print("I really like pizza")

