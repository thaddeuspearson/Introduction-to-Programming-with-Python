# Will an error occur if you try to access a list element with an index greater 
# than or equal to the list's length? For example:

"""
foo = ['a', 'b', 'c']
print(foo[3])      # will this result in an error?
"""

# Yes. since foo only has 3 elements, the 3rd index is out of range. This will
# raise an IndexError.
