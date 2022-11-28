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


x = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45]
print(highests(x))
