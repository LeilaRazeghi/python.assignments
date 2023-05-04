n=int(input("enter your snake length:"))

for i in range(n):
    if i%2==0:
        print("#", end="")

    else:
        print("*", end="")