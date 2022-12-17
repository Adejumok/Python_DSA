def sum_diagonal(arr):
    """
    :param arr:
    :return: arr[0][0] + arr[1][1] + arr[2][2]...
    """
    diag_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                diag_sum += arr[i][j]
    return diag_sum


x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_diagonal(x))
