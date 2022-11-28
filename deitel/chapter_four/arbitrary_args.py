
def average(*nums):
    return sum(nums) / len(nums)


print(average(9, 4, 5, 2))
scores = [60, 50, 40]
print(average(*scores))

colors = ['red', 'orange', 'yellow']
print(list(enumerate(colors)))
# Out[16]: [(0, 'red'), (1, 'orange'), (2, 'yellow')]

"""Displaying a bar chart"""
numbers = [19, 3, 15, 7, 11]
print(numbers.index(7))
print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8} Bar')
for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8} {"*" * value}')
