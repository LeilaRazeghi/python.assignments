import qrcode

name=input("enter your name: ")
cellnumber=input("enter your your cellphone no: ")

img=qrcode.make(name+ cellnumber)

img.save("your qrcode.png")