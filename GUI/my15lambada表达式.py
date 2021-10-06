# 崔浩然
# 时间:2021/10/6 15:14
# 功能：测试lambada表达式
from tkinter import *

root =Tk()

root.geometry('270x50')

def mouseTest1():
    print('command方式，简单情况：不涉及获取event对象，可以使用')
    
def mouseTest2(a,b):
    print("a={0},b={1}".format(a,b))
    
Button(root, text="测试command1", command=mouseTest1).pack(side="left")

Button(root, text="测试command2", command=lambda:mouseTest2('gaoqi',"xixi")).pack(side="left")
root.mainloop()

