# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size, text = "I love python"):
    print(f"My size is: {size}")
    print(f"Text on t-short is: {text}")
make_shirt("M")

def make_shirt(size, text = "adidas"):
    print(f"My size is: {size}")
    print(f"Text on t-short is:{text}")
make_shirt("L")

def make_shirt(size, text = "asics"):
    print(f"My size is: {size}")
    print(f"Text on t-short is:{text}")
make_shirt("XL")
