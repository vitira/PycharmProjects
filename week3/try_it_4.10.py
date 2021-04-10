# 4.10 Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that
# do the following.
favorite_car = ["bmw", "subaru", "audi", "porsche", "mercedes", "tesla", "zaz"]
print(favorite_car)
#### Print the message, The first three items in the list are:. Then use a slice to print the first three items from
# that program’s list.
print(f"The first three items in the list are: {favorite_car [:3]}")
# Print the message, Tree items from the middle of the list are: Use a slice to print three items from the middle of
# the list.
print(f"Three items from the middle of the list are: {favorite_car [2:5]}")

#### Print the message, The last three items in the list are: Use a slice to print the last three items in the list.
print(f"The last three items in the list are: {favorite_car [-3:]}") ####??????