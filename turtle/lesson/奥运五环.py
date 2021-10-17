# 崔浩然
# 时间:2021/10/16 21:34
# 功能：turtle画奥运五环
from turtle import *
speed(0)
pensize(9)  # 线条的粗细
color('black')
circle(75)

penup()
goto(-180, 0)
pendown()

color('blue')
circle(75)

penup()
goto(180, 0)
pendown()

color('green')
circle(75)

penup()
goto(80, -100)
pendown()

color('red')
circle(75)

penup()
goto(-80, -100)
pendown()

color('yellow')
circle(75)

mainloop()
