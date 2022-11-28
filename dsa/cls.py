lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def find_missing(arr, number):
    temp_arr = []
    temp_arr.extend(arr)
    arr.remove(number)
    return temp_arr.index(number)


print(f'The initial list is {lst}')
print(f'The number removed was from index {find_missing(lst, 7)}')
