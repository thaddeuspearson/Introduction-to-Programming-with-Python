# Without running this code, what will it print? Why?

"""
1. dict1 = {
2.     "Hitchhiker's Guide to the Galaxy": 42,
3.     'Monty Python': 'The Life of Brian',
4.     'Airplane!': "Don't call me Shirley!",
5. }
6.
7. dict2 = dict(dict1)
8. dict2['Monty Python'] = 'Holy Grail'
9. print(dict1['Monty Python'])

 This will print 'The Life of Brian', because even though a shallow copy was
 made on line 7, The keys and values of everything in dict1 are immutable
 types (strings in this case). This means that when dict2 changed the value at
 its key 'Monty Python', a new string was created in its place in memory,
 which is not the same location as dict1's 'Monty Python' location in memory.
"""

