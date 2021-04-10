#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-
#else chain.
color = ["green", "yellow", "red"]
#### If the alien is green, print a message that the player earned 5 points.
if "green" in color:
    print("you earned 5 point")
#### If the alien is yellow, print a message that the player earned 10 points.
elif "yellow":
    print("you earned 10 point")
#### If the alien is red, print a message that the player earned 15 points.
else:
    print("you earned 15 points")
#### Write three versions of this program, making sure each message is printed
#for the appropriate color alien.
color = ["green", "yellow", "red"]
if "green" in color:
    print(5)
if "yellow":
    print(10)
if "red":
    print(15)