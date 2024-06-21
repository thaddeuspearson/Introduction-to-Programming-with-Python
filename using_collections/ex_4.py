# Consider the following dictionary:

"""
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}
"""

# 1. Write some code to print Bark by accessing the element associated with the
# key Dog.

print(pets["Dog"])

# 2. Part 2: Write some code to print None when you try to print the value
# associated with the non-existent key, Lizard.

print(pets.get("Lizard"))

# 3. Part 3: Write some code to print <silence> when you try to print the value
# associated with the non-existent key, Lizard.

print(pets.get("Lizard", "<silence>"))

