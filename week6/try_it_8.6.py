# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned.

def city_country(name, country):
    return f"{name.title()}, {country.title()}"



c = city_country("kiev", "ukraine")
print(c)

d = city_country("hong kong", "china")
print(d)