class Extreme:

    print('Enter 12 numbers')
    numberCount = 1
    lst = []

    while numberCount <= 12:
        number = int(input('Enter the next number: '))
        lst.append(number)

        numberCount = numberCount + 1

    print(f"Minimum: {min(lst)}")
    print(f'Maximum: {max(lst)}')
    print(f'The sum of the extremes(i.e the minimum and the maximum values) is: {min(lst) + max(lst)}')
