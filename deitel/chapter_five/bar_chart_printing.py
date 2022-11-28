class bar_chart:
    temp_list=[]
    numberCount= 1

    print('Enter five numbers between 1 and 30')
    while numberCount <= 5:
        number = (int(input('Enter number: ')))
        temp_list.append(number)
        numberCount += 1

    for n in temp_list:
        print('*' * n)

