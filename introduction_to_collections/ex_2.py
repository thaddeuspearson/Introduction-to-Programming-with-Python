# Can you write some code to change the value 'bye' in the following tuple to
# 'goodbye'?

"""
stuff = ('hello', 'world', 'bye', 'now')
"""

# The items in a tuple are not able to be changed because a tuple is immutable.
# Therefore I need to create a new tuple from indexes of the old tuple

new_stuff = (stuff[0], stuff[1], stuff[3])

