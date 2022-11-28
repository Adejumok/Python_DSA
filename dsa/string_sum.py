def int_to_string(arr, k):
    sum_arr = []
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == k:
                str_sum = f"{arr[i]}+{arr[j]}"
                sum_arr.append(str_sum)
    return sum_arr


x = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
print(int_to_string(x, 9))
