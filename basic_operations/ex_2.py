# Use the REPL and the arithmetic operators to extract the individual digits of 4936:

"""
One place is 6.
Tens place is 3.
Hundreds place is 9.
Thousands place is 4.
"""

num = 4936

places = {
    "ones" : None,
    "tens" : None,
    "hundreds" : None,
    "thousands" : None,
}

print(f"Num is {num}")

for place in places.keys():
    places[place] = num % 10
    num = num // 10
    print( f"The digit in the {place} place is: {places[place]}")
