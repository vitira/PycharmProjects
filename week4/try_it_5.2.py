# 5.2 More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
####Tests for equality and inequality with strings
car = "volvo"
#print("car is audi. I presume False")
print(car == "audi")

car = "opel"
#print("car is honda. I expect True")
print(car != "honda")

#### Tests using the lower() function
car = "Mazda"
print(car.lower() == "mazda")

car = "land rower"
print(car.title() == "Land Rower")

car = "land rower"
####print(car.camel() == "Land Rower")???????????????????????????????????????????

#### Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
number = 2
print(number == 3)
print(number < 3)

number = 21
number <= 21 # TRUE
number < 21 # FALSE

number = 100000
print(number <= 5550000000)


####Tests using the and keyword and the or keyword
number = 5
print(number <= 5 and number >= 3) #True

print(number >=10 and number ==5) #False

print(number >= 25 or number >=1) #True

#### Test whether an item is in a list
car = ["honda", "toyota", "audi", "vw", "jiguli"]
print(car == "bmw")#False

print(car != "lada")#True

print("fahjkl" in car)
print("honda" in car)

#### Test whether an item is not in a list
car = ["audi", "bmw", "lincoln"]
print("lancia" in car)#false