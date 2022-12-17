def recursive_bin_search(lst, target):
    i = 0
    mid_lst = len(lst) // 2
    while i < len(lst):
        if lst[i] == target:
            return i
        elif lst[i] < target:
            recursive_bin_search(lst[:mid_lst], target)
        else:
            recursive_bin_search(lst[mid_lst:], target)
    return None


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(recursive_bin_search(x, 3))
