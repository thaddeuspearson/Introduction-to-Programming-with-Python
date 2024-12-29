# In your own words, explain the difference between these two expressions.

"""
my_object1 == my_object2
my_object1 is my_object2
"""

"""
 The `==` operator is testing for equality between my_object1 and my_object2. It
 will return True if both objects contain the same objects as one another,
 respective of the object types the variables are referencing. However, the 
 elements contained within the objects do not have to be stored in the same 
 places in memory, they simply need to be identical.

 The `is` keyword tests for equality between my_object1 and my_object2
 similarly to the `==` operator, however, `is` looks to see that the object
 referenced by these variables are both stored in the same memory location, so
 they actually are the same exact object in memory.
 """


