from turtle import *


speed(0)
def curvemove(): #曲线函数
    for i in range(200):
        right(1)
        forward(1)


color('red', 'pink')
begin_fill()
left(140)
forward(111.65)
curvemove() #画曲线
left(120)
curvemove() #画曲线
forward(111.65)
end_fill()

penup()
goto(100,200)
write("祝爸妈身体健康",font = ("Times", 30, "bold"))
done()