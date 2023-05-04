import math

number=int(input("enter your number: "))
i=1

while True:
        
    if number % i !=0:
        print("no")
        break

    elif number % i==0:
        number=number/i

        if number==1:
         print("yes")
         break

        else:
           i=i+1