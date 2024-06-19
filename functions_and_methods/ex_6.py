# What does the following code print?

"""
def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')
"""

# This code prints nothing to the console. the return statement on the third
# line of the function definition has the return statement which stops
# execution, so the print statement on the fourth line is never reached.
