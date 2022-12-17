def highests(lst):
    temp = []
    second_highest = lst[0]
    highest = lst[0]
    for i in lst:
        if i > highest:
            highest = i
    for i in lst:
        if second_highest < i < highest:
            second_highest = i

    temp.append(highest)
    temp.append(second_highest)
    return temp


def highest_two(lst):
    two_h = []
    h = 0
    high1 = lst[0]
    high2 = lst[0]

    while h < len(lst):
        if lst[h] > high1:
            high2 = high1
            high1 = lst[h]
    two_h.append(high1)
    two_h.append(high2)
    return two_h


x = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45]
print(highests(x))
