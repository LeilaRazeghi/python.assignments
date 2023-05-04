
first_list = []
length_list = int(input(" enter length list: "))

for i in range(length_list):
    number = int(input("enter number(i + 1): "))
    first_list.append(number)

new_list = []
for number in first_list:
    if number not in new_list:
        new_list.append(number)

print(new_list)    