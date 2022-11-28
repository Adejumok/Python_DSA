def two_sum(arr, target):
    temp_arr = []
    for i in arr:
        for j in arr:
            if i + j == target:
                temp_arr.append(arr.index(i))
                temp_arr.append(arr.index(j))
                return temp_arr


print(f'The sum up to the target is found at index {two_sum([2, 7, 5, 3, 9, 8, 1], 15)}')
