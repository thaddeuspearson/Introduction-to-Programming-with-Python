# What happens when you run the following code? Why?

"""
NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)
"""

# This code prints 6 statements, first with the name Victor, next with the name
# Nina. While this code runs without error, it is not best practice to 
# re-assign a constant variable (in this case NAME). The writer of this code 
# should refactor this variable to be lowercase if reassignment like this is 
# going to occur.
