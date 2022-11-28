counter = 1
temp_list = []
print("Enter 10 numbers")

while counter <= 10:
    integer = int(input("Enter the next number: "))
    temp_list.append(integer)
    counter += 1

largest_number = temp_list[0]
for n in temp_list:
    if n > largest_number:
        largest_number = n

print(f"Largest number is: {largest_number}")
