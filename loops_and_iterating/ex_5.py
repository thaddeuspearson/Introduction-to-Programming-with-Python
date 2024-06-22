# Print all of the even numbers in the following list of nested lists. Don't
# use any while loops.

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

flat_list = []

for l in my_list:
    flat_list.extend(l)

for num in flat_list:
    if num % 2 == 0:
        print(num)
