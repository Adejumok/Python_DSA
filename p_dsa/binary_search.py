def binary_search(arr, target):
    first_digit = 0
    last_digit = len(arr) - 1
    mid_point = (first_digit + last_digit) // 2

    while first_digit <= last_digit:
        if arr[mid_point] == target:
            return mid_point
        elif mid_point > target:
            first_digit = mid_point + 1
        else:
            last_digit = mid_point + 1
    return None


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(x, 12))
