# Without running the following code, what do you think it will do?

"""
def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)
"""

# This code will throw a SyntaxError, as parameters with default arguments
# must be defined after all parameters that do not have default values provided
# for them.
