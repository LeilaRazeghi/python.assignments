import random

n=int(input("enter number less than 10:"))
array=[]

while len(array)<n:
    num=random.randint(1, n)

    if num in array:
        print(array)
    else:
        array.append(num)
