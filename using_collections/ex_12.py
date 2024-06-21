# Write some code that determines and prints whether the number 3 appears
# inside each of these lists:


numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

for num in [numbers1, numbers2, numbers3, numbers4, numbers5]:
    print(3 in num)

