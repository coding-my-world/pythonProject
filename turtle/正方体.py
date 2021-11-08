from turtle import *
x=10
speed(10)
penup()
while True:
    goto(x, 0)
    pendown()
    for i in range(4):
        color('red')
        fd(10)
        right(90)
    x += 20
    penup()
mainloop()
