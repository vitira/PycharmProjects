#5.4 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
#write an if-else chain.
color = "green"
if "red" in color:
    print("it is not right color")
else:
    print("it is green color")

#### If the alien’s color is green, print a statement that the player just earned
#5 points for shooting the alien.
color = "green"
if "green" in color:
    print("player just earned 5 points")
####If the alien’s color isn’t green, print a statement that the player just earned
#10 points.
color = "green"
if "white" in color:
    print("player just earned 222 point")
else:
    print("player just earned 10 point")
####Write one version of this program that runs the if block and another that
#runs the else block
car = "subaru"
if "subaru" in car:
    print("right")
else:
    print("wrong")

bike = "ducati"
if "honda" in bike:
    print("japan bike")
else:
    print("italian bike")