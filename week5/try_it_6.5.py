# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
#### Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
#### Use a loop to print the name of each river included in the dictionary.
#### Use a loop to print the name of each country included in the dictionary.

rivers = {
    "nile": "egypt",
    "dnipro": "ukraine",
    "lena": "russia"
}
for key, value in rivers.items():
    print(f"The {key.title()} is biggest river in {value.title()}.")

print("-----------------------------------")

for key in rivers.keys():
    print(key.title())

print("____________________________________")

for key in rivers:
    print(key.title())

print("=====================================")

for value in rivers.values():
    print(value.title())