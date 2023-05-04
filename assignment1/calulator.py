import math
print("welcome to my calculator")
print("+: sum")
print("-: sub")
print("*: mul")
print("/: div")
print("sin")
print("cos")
print("tan")
print("cot")
print("log")
print("sqrt")
print("factorial")
print("please enter your choice")
op=input()

if op=="+"or op=="-" or op=="*" or op=="/":
    a=float(input("enter first number: "))
    b=float(input("enter second number: "))

else:
    a=int(input("enter first number:"))

if op=="+":
    result=a+b
elif op=="-":
        result=a-b
elif op=="*":
      result=a*b
elif op=="/":
      if b==0:
            result= "can not divide by zero"
      else:
          result=a/b

if op=="sin"or op=="cos"or op=="tan"or op=="cot":
     result=a/180*math.pi
     
elif op=="sin":     
     result=math.sin(a)
elif op=="log":
      result=math.log(a)
elif op=="sqrt":
     if a<0:
        result="no root"
     else:
        result=math.sqrt(a)
elif op=="cos":
     result=math.cos(a)
elif op=="tan":
     result=math.tan(a)   
elif op=="cot":
     result=1/math.tan(a)

elif op=="factorial":
    if a>0 and a % 1==0:
     result=math.factorial(a)

    else:
     result="ivalid number"

print(result)