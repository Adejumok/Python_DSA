def count_recursion(lst):
    count = 0
    c = 0
    while c < len(lst):
        count = 1 + count_recursion(lst[1:])
    return count
