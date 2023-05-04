a=float(input("enter side a:"))
b=float(input("enter side b:"))
c=float(input("enter side c:"))

if(a+b>c)and(a+c>b)and(b+c>a):
    print("It can be drawn")
else:
    print("can not be drawn")