# Without running the following code, what do you think it will do?

"""
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)
"""

# This code will print the single argument given in the invocation, and then
# print the two default arguments given in the function definition, as those
# positional arguments were not provided in the invocation.
