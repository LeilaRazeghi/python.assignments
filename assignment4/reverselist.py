
first_list = []
length_list = int(input(" enter length list : "))

for i in range(length_list):
    number = input("enter number(i + 1): ")
    first_list.append(number)

reversed_list = []
for j in range(length_list - 1, -1, -1):
    reversed_list.append(first_list[j])  

print(reversed_list)  
