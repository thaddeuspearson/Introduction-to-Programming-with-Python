# What does this program print? Why?

"""
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)
"""

# This will print 'bar' as foo is defined in the global scope. The foo variable 
# defined within the set_foo function is shadowing the foo variable in the
# global scope, and does not reassign it.
