# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type = '', location = ''):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restauran_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.number_served = 0

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

    def customer_number(self):
        """Show costumers number"""
        print(f"Restaurant served {str(self.number_served)} seats.")

    def set_number_served(self, seats):
        """Served customers"""
        self.number_served = seats
        print(f"Number of seats is: {str(self.number_served)}")

    def increment_number_served(self, seats):
        """Add served customers"""
        self.number_served += seats

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, location, flavors):
        self.flavors = flavors
        super().__init__(restaurant_name, cuisine_type, location)

    def pick_flavors(self):
        print(f"Flavors is: {self.flavors}")

restaurant_costumer = Restaurant("Salt", "Seafood", "New Brunswick")
restaurant_costumer.customer_number()
restaurant_costumer.set_number_served(25)
#restaurant_costumer.set_number_served(1000)
restaurant_costumer.increment_number_served(2000)
restaurant_costumer.customer_number()

ice_cream = IceCreamStand("Tomas sweet", "desert", "New Brunswick", ["chocolate", "vanilla", "coffee"])
ice_cream.pick_flavors()
