# 崔浩然
# 时间:2021/10/17 12:30
# 功能:turtle画星星

from turtle import *
from random import *
speed(0)
setup(600,600)
bgcolor('black')
colormode(255)
pensize(100)

goto(-300,200)
fd(700)

color(50,50,50)
penup()
goto(-300,100)
pendown()
fd(700)

color(75, 75, 75)
penup()
goto(-300, 0)
pendown()
fd(700)

color(100, 100, 100)
penup()
goto(-300,-100)
pendown()
fd(700)

color(125,125,125)
penup()
goto(-300,-200)
pendown()
fd(700)

color(150,150,150)
penup()
goto(-300,-300)
pendown()
fd(700)

# 画星星
color('yellow')
pensize(1)
for l in range(8):
    print(l)
    x=randint(-200,200)
    y=randint(-200,200)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(4):
        forward(15)
        left(30)
        forward(15)
        right(120)
    end_fill()

    penup()

mainloop()