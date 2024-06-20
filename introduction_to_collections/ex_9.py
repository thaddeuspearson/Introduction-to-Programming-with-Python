# Given the following code, answer the questions and explain your
# answers:

"""
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)
"""

# 1. Are the lists assigned to my_list and another_list equal?
    # Yes, both lists contain the same elements and would return True if
    # compared with "==".

# 2. Are the lists assigned to my_list and another_list the same object?
    # No. they are two distinct lists.

# 3. Are the nested lists at index 3 of my_list and another_list equal?
    # Yes, if compared with "==", the result would be True

# 4. Are the nested lists at index 3 of my_list and another_list the same object?
    # Yes, as using the list() literal only makes shallow copies of nested
    # lists.

