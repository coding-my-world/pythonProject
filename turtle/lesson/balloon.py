# 崔浩然
# 时间:2021/10/17 12:06
# 功能：turtle画气球

from turtle import *
import random

colormode(255)
penup()
speed(0)
for i in range(10):
    
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    x=random.randint(-220,220)
    y=random.randint(-100,220)
    goto(x,y)
    pendown()
    color(red,green,blue)
    begin_fill()
    circle(30)
    end_fill()
    right(90)
    forward(30)
    left(90)
    penup()
mainloop()
