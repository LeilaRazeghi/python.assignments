
import turtle

turtle.bgcolor("black")

colors=["white","orange", "green", "yellow", "purple", "gold", "pink", "violet", "red", "blue", "turquoise", "light green"]

p=turtle.Pen()
p.shape("turtle")

initial_angle=30
initial_side=3
xcordinate=3
initial_length=20

while initial_side<39:
    p.pencolor(colors[(initial_side-3)%12])
    p.left(initial_angle)

    for i in range(initial_side):
        p.left(360/initial_side)
        p.forward(initial_length)
    p.penup()
    p.goto(xcordinate, 0)
    p.pendown()
    initial_angle=(360/initial_side -360/(initial_side+1))/2
    
    initial_side +=1
    xcordinate +=5
    initial_length *=1.07

turtle.done()


















n=3
while n<11:
    p.up()
    p.setpos(20*(n-3),0)
    p.down()
    p.pencolor("red")
    zavieh_charkhesh= 180-((n-2)*180)/n
    p.setheading(zavieh_charkhesh+(n-2)*180/n/2)
    for j in range(n):
        p.forward(50+8*(n-3)) #15
        p.left(zavieh_charkhesh)

    n+=1

turtle.done()