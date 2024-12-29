# What happens when you run the following program? Why do we get that result?

"""
def set_foo():
    foo = 'bar'

set_foo()
print(foo)
"""

# A NameError occurs as foo is locally scoped to the set_foo function.
