w=float(input("enter your weight in kilograms:"))
h=float(input("enter your height in square meters:"))

if w<0 or h<0:
     print("invalid")
else: 
  BMI=w/(h**2)

if BMI<18.5:
   print("under weight")

elif BMI==18.5-24.9:
    print("normal weight")

elif BMI==25-29.9:
     print("over weight")

elif BMI==30-3.9:
      print("obesity")

elif BMI==35-39.9:
       print("extreme obesity ")
       
print(BMI)