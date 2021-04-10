# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.


# positional argument
def make_shirt(size, text):
    """Should print the size of the shirt and the message printed on it"""
    print(f"The shirt size is: {size}")
    print(f"The text on shirt is: {text} ")
make_shirt("M", "USA")
print("")
make_shirt("S", "Puma")

# keyword argument
print("=========================================")

def make_shirt(size = "s", text = "Puma"):
    print(f"The shirt size is: {size}")
    print(f"The text on shirt is: {text} ")
make_shirt(size = "s", text = "Puma")
