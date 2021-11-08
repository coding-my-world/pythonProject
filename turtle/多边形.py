from turtle import *
x=10
speed(0)
penup()
for j in range(5):
    goto(x, 0)
    pendown()
    for i in range(3):
        color('red')
        fd(50)
        left(120)
    x += 100
    penup()

y=-50
x=0
for j in range(6):
    goto(x, y)
    pendown()
    for i in range(6):
        color('red')
        fd(20)
        left(72)
    x += 50
    penup()
    
    
y=-200
x=0
for j in range(6):
    goto(x, y)
    pendown()
    for i in range(6):
        circle(30)
    x += 70
    penup()
mainloop()

