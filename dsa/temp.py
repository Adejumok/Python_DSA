

temp_num=int(input("Enter the number of temperatures: "))
count = 0
sum_ = 0
temp_list= []
greater_than_avg =[]
while count < temp_num:
    temp = float(input("Enter the temperature: "))
    temp_list.append(temp)
    sum_ += temp
    count = count + 1
aveg = sum_/count
for t in temp_list:
    if t > aveg:
        greater_than_avg.append(t)

print(greater_than_avg)


