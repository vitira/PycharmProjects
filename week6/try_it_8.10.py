def magician_name(magicians):
    """List of magician name"""
    for magician in magicians:
        msg = "Hello: " + magician + "!"
        print(msg)

def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = magician + " the Great"
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ["aaaaa", "sssss","ddddd"]
magician_name(magicians)

make_great(magicians)
magician_name(magicians)