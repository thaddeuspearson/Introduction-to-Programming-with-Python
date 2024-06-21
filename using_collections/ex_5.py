# Which of the following values can't be used as a key in a dict object, and
# why?

"""
'cat'                           # can
(3, 1, 4, 1, 5, 9, 2)           # can
['a', 'b']                      # cannot, lists are mutable
{'a': 1, 'b': 2}                # cannot, dicts are mutable
range(5)                        # can
{1, 4, 9, 16, 25}               # cannot, sets are mutable
3                               # can
0.0                             # can
frozenset({1, 4, 9, 16, 25})    # can
"""

