# Without running this code, what will it print? Why?

"""
1. set1 = {42, 'Monty Python', ('a', 'b', 'c')}
2. set2 = set1
3. set1.add(range(5, 10))
4. print(set2)
"""

# This will print {42, 'Monty Python', ('a', 'b', 'c'), range(5,10)}, since a
# shallow copy was made on line 2, and both set1 and set2 point to the same set
# in memory. Since this is a set, the order of the elements moght now print in
# the exact same order.

