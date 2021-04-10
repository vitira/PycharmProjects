full_name = "Metthew McConaughey"
msg = "hiking in Hawai."
print(full_name + " "+msg.replace('.', '!!!'))

#f"{full_name} {msg.replace ('.', '!!!!!!!!')}"

print(f"\t{full_name}\t\n{msg.replace ('.', '!+++++')}")

for number in range(0, 11):
    for number2 in range(0, 11):
        print(f"{number * number2}", end = "\t")
    print(" ")

city = {"Country": "Ukraine", "Capital": "Kiev", "age": "1500 years"}
city2 = {"Country": "Germany", "Capital": "Berlin", "age": "800 years"}
city3 = {"Country": "England", "Capital": "London", "age": "2000 years"}
city4 = {"Country": "USA", "Capital": "Washington", "age": "230 years"}

citys = [city, city2, city3, city4]

print(citys[0])
print(city4["Capital"])
print(citys[0]["Capital"])
print(city["Capital"])

print(" ")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
for value in city.values():
    print(value)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")



for city in citys:
    print(city["Country"], end = "\t")
    print(city["Capital"], end = "\t")
    print(city["age"], end = "\t")
    print("")

print('==============================================================================================')

name = input("What is your name")
print("Hello" + name + "!")