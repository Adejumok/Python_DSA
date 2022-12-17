def max_no(arr):
    max_ = arr[0]
    n = 0
    while n < len(arr):
        if arr[n] > max_:
            max_ = arr[n]
    return max_


l = [3, 4, 5]
print(max_no(l))
