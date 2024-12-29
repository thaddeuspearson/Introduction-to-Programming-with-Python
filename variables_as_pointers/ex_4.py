# Without running this code, what will it print? Why?

"""
1. dict1 = {
2.    'a': [1, 2, 3],
3.    'b': (4, 5, 6),
4. }
5. 
6. dict2 = dict(dict1)
7. dict1['a'][1] = 42
8. print(dict2['a'])

This will print [1, 42, 3] since a shallow copy was made on line 6. When this
happened, all the keys and values were stored in a new memory location.
However, because the value of the key 'a' was a mutable type (in this case, a
list), what was copied was the pointer to the memory location of the list, not
the list itself. 

When the python interpreter reassigned the 1st index of 'a' in dict1, it
changed the element at the memory address that was pointed to by both 'a' keys
in dict1 and dict2. In this case a deepcopy should have been done to ensure
this likely unwanted behavior would have been avoided.
"""

