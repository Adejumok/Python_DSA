def sum_recursion(lst):
    i = 0
    sum_ = 0
    while i < len(lst):
        sum_ = lst[i] + sum_recursion(lst[1:])
    return sum_


l = [3, 4, 5]
print(sum_recursion(l))
