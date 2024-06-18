# Write a program named greeter.py that greets 'Victor' three times. Your
# program should use a variable and not hard code the string value 'Victor' in
# each greeting. Here's an example run of the program:

"""
$ python greeter.py
Good Morning, Victor.
Good Afternoon, Victor.
Good Evening, Victor.
"""

name = "Victor"
times = ["Morning", "Afternoon", "Evening"]

for time in times:
    print(f"Good {time}, {name}.")
