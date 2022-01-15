def magician_name(magicians):
    """List of magician name"""
    for magician in magicians:
        msg = "Hello: " + magician + "!"
        print(msg)

magician_name_list = ["Mark", "Serg", "Kato"]
magician_name(magician_name_list)


magician_name_list2 = ["Mark$$$", "Serg$$$", "Kato$$$"]
magician_name(magician_name_list2)