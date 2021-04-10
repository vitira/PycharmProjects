# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, location = ''):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restauran_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location

describe_restaurant = Restaurant("Sahara", "Mediterian", "New Bruncwick")
print(f"Restaurant name is: {describe_restaurant.restauran_name} where cousine is {describe_restaurant.cuisine_type} "
      f"and locate in {describe_restaurant.location} is good one and not expensive.")

describe_restaurant = Restaurant("Salt", "Seafood")
print(f"Restaurant name is {describe_restaurant.restauran_name} and cousine type is {describe_restaurant.cuisine_type}")

describe_restaurant = Restaurant("Yellow Tail", "Asian", "Las Vegas")
print(f"Restaurant name is {describe_restaurant.restauran_name} cousine type is {describe_restaurant.cuisine_type} "
      f"whisch located in {describe_restaurant.location} is kind of expensive one.")