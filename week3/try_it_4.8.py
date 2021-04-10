# 4.8 Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python
# Make a list of first 10 cubes(that is, the cube of each integer from 1 through 10) and use for a loop to print out
# the value of each cube.

valllue = [number ** 3 for number in range(1, 11)]
print(valllue)
print("\n")

valllue = []
for number in range(1, 11):
    squere = number ** 3
    valllue.append(squere)
    print(valllue)
print("\n")

number = []
for something in range(1, 11):
    number.append(something ** 3)
    print(number)
