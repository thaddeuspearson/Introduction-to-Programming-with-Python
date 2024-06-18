# Modify the greeter.py program to ask for the user's first and last names
# separately, then greet the user with their full name.

"""
$ python greeter.py
What is your first name? Bob
What is your last name? Roberts
Hello, Bob Roberts!
"""

prefix = "What is your "
first = input(prefix + "first name? ")
last = input(prefix + "last name? ")
print(f"Hello, {first} {last}!")
