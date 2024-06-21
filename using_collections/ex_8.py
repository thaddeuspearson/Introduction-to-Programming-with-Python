# Explain why the code below prints different values on lines 3 and 4.

"""
text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29
"""

# On line 3, a new list is created from slicing, so the indexes are no
# longer the same as they are on line 4.

