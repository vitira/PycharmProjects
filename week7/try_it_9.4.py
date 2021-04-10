# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.

# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.

# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any num-
# ber you like that could represent how many customers were served in, say, a
# day of business.

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
        #print(f"Incremented number served {str(self.increment_number_served)}")





restaurant_costumer = Restaurant("Salt", "Seafood", "New Brunswick")
restaurant_costumer.customer_number()
restaurant_costumer.set_number_served(25)
#restaurant_costumer.set_number_served(1000)
restaurant_costumer.increment_number_served(2000)
restaurant_costumer.customer_number()



