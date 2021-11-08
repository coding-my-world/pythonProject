# 崔浩然
# 时间:2021/11/2 20:06
# 功能：上课代码
import turtle
import random

t=turtle.Pen()
t.speed(0)
colors=["red","yellow", "blue","green"]
for x in range(100):
    color=random.randint(0, 3)
    # print(color)
    t.pencolor(colors[color])
    t.forward(x)
    t.left(91)
