# 崔浩然
# 时间:2021/10/26 8:00
# 功能：turtle绘制山西老陈醋醋坛子

from turtle import *

colormode(255)
hideturtle()
speed(0)
color(0,0,0)
begin_fill()
right(30)
circle(200,60)
left(-240)
circle(200,60)
end_fill()
color(65,11,23)
begin_fill()
goto(0,-20)
left(120)
circle(200,60)
goto(200,0)
left(180)
circle(-200,60)
end_fill()

left(90)
goto(0,-20)
circle(300,60)

right(-30)
circle(200,60)
left(-240)
circle(200,60)

color(65,11,23)
begin_fill()
goto(0,-340)
left(120)
circle(200,60)
goto(200,-320)
left(180)
circle(-200,60)
end_fill()


penup()
goto(200,-320)
pendown()
color("brown")
begin_fill()
right(90)
circle(300,60)
right(90)
circle(200,-60)
left(270)
circle(300,60)
left(30)
circle(200,60)
end_fill()

penup()

goto(160,-200)
pendown()
color("red")
begin_fill()
left(100)
fd(100)
left(90)
fd(100)
left(90)
fd(100)
left(90)
fd(100)
end_fill()
penup()
goto(70,-210)
pendown()
color("black")

write("醋",font = ("Times", 30, "bold"))
penup()
goto(200,0)
pendown()
write('山西老陈醋',font=("楷体",30,"normal"))
mainloop()