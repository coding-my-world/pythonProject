# 崔浩然
# 时间:2021/10/6 15:35
# 功能：绑定事件样例演示
from tkinter import *
root=Tk()
root.geometry("200x70")
def mouseTest1(event):
    print("bind（）方法绑定，还可以获取到event对象")
    print(event.widget)
    
def mouseTest2(a,b):
    print("a={0},b={1}".format(a,b))
    print('command方式绑定，不能直接获取到event对象')
    
def mouseTest3(event):
    print("中键单击事件，绑定给所有按键拉")
    print(event.widget)

b1=Button(root, text="测试bind（）绑定")
b1.pack(side="left")
#bind方式绑定事件
b1.bind("<Button-1>",mouseTest1)

#command属性直接绑定事件
b2 = Button(root, text = "测试command2", command=lambda :mouseTest2("gaoqi","xixi"))
b2.pack(side="left")

#给所有Button按钮都绑定中键单击事件<Button-2>
b1.bind_class("Button","<Button-2>",mouseTest3)
root.mainloop()