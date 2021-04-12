##6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
#up the code from Exercise 6-3 (page 102) by replacing your series of print
#statements with a loop that runs through the dictionary’s keys and values.
#When you’re sure that your loop works, add five more Python terms to your
#glossary. When you run your program again, these new words and meanings
#should automatically be included in the output.

glossary = {
    "dictionary": "collect data similar like list",
    "list": "collect data",
    "if": "help as work with loop",
    "loop": "help us run data step by step",
    "variable": "it is dynamic information",
    "elif": "it is a part of information",
    "else": "it is rest information",
    "conditional test": "return True or False",
    "title": "output first letter big",
    "string": "some information in memory, word and number combination",
    }
for key, value in glossary.items():
    print(f"this is key: {key}")
    print(f"this is value: {value}")
    print("")