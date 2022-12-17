def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    left_side, right_side = split(lst)
    left = merge_sort(left_side)
    right = merge_sort(right_side)
    return sorted_merge(left, right)


def split(lst):
    mid_point = len(lst) // 2
    left = lst[:mid_point]
    right = lst[mid_point:]
    return left, right


def sorted_merge(left_side, right_side):
    i = 0
    j = 0
    l = []

    while i < len(left_side) and j < len(right_side):
        if left_side[i] < right_side[j]:
            l.append(left_side[i])
            i += 1
        else:
            l.append(right_side[j])
            j += 1
    while i < len(left_side):
        l.append(left_side[i])
        i += 1
    while j < len(right_side):
        l.append(right_side[j])
        j += 1

    return l


arr = [4, 3, 2, 8, 5, 9, 1, 6, 7]
print(merge_sort(arr))
