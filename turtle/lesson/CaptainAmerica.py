# 崔浩然
# 时间:2021/10/16 22:02
# 功能:turtle画美国队长的盾牌

from turtle import *
speed(0)
penup()
goto(0,-200)
pendown()
color('red')

begin_fill()
circle(200)
end_fill()

penup()
goto(0,-150)
pendown()
color('white')

begin_fill()
circle(150)
end_fill()


penup()
goto(0,-100)
pendown()
color('red')

begin_fill()
circle(100)
end_fill()

penup()
goto(0,-50)
pendown()
color('blue')

begin_fill()
circle(50)
end_fill()

penup()
goto(-40,15)
pendown()

color('white')
begin_fill()
for i in range(5):
    forward(80)
    right(144)
end_fill()
mainloop()
