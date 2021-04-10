#4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
#simple foods, and store them in a tuple.
buffet_food = ("meatball", "cabagerolls", "kyiv_meatball", "mash_potato", "peroge")

#### Use a for loop to print each food the restaurant offers.
for buffet in buffet_food:
    print(buffet)
print()
####  Try to modify one of the items, and make sure that Python rejects the
#change.
#buffet_food[0] = "cheecken_meatboll"
#print(buffet_food)

#### The restaurant changes its menu, replacing two of the items with different
#foods. Add a block of code that rewrites the tuple, and then use a for
#loop to print each of the items on the revised menu.
buffet_food = ("cheecken_meatball", "cabagerolls", "kyiv_meatball", "mash_potato", "peroge_with_cheese")
for buffet in buffet_food:
    print(buffet)