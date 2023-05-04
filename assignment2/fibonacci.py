# Fibonacci sequence

n=int(input("eneter the number of elements:"))
a=0
b=1

for i in range(n):
    print(a,end="")
    a, b=b, a+b
