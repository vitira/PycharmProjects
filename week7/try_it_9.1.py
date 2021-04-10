# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
# that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type = '', location = ''):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restauran_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location

    def describe_restaurant(self):
        """Describe the restaurant"""
        if self.location != '':
            print(f"{self.restauran_name} have {self.cuisine_type} cuisine wich located in {self.location}")
        elif self.cuisine_type == '' and  self.location =='':
            print(f"{self.restauran_name}")
        else:
            print(f"{self.restauran_name} have {self.cuisine_type} cuisine")

    def open_restaurant(self):
        print(f"{self.restauran_name} is open. You are welcome. Enjoy.")


new_restaurant = Restaurant("Salt", "Seafood", "New Brunswick")
print(new_restaurant.restauran_name)
print(new_restaurant.cuisine_type)
print(new_restaurant.location)

new_restaurant.describe_restaurant()

new_restaurant.open_restaurant()

def hello():
    print("Hello")


hello()






res = Restaurant("My Lovely Wife Restaurant")
res.open_restaurant()
print('________________________________')

# myres = Restaurant("Veganized", "Vegan")
# myres.describe_restaurant()
# print(myres.cuisine_type)
#
# myres3 = Restaurant("Yellow Tail", "Asian", "Los Vegas")
# myres3.describe_restaurant()
#
# myres2 = Restaurant("Sahara", "Mediterranian")
# myres2.describe_restaurant()
#
# print("------------------")
# mylist = [11, 7, 92, 35, 32, 2]
# print(mylist.pop(2))
# print(mylist)