# 崔浩然
# 时间:2021/9/24 21:23
# 功能:第一个GUI界面

from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('我的第一个GUI程序')
root.geometry("500x300+1000+200")
button1 = Button(root)
button1['text'] = '点我'
button1.pack()


def dianwo(e):         # e就是事件对象
    messagebox.showinfo("Message", "叫你点你就点?")


button1.bind("<Button-1>",dianwo)
root.mainloop()        # 调用组件的mainloop()方法，进入事件循环
