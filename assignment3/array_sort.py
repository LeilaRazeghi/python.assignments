
n=int(input("enter array size:"))
myarray=[]

for i in range(n):
    myarray.append(int(input("eneter element:")))

for i in range(1, n):
    if myarray[i]<myarray[i-1]:
        print("not sorted")
        break

    else:
        print("sorted")