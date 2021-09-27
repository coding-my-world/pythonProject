# 崔浩然
# 时间:2021/9/29 11:33
# 功能：
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.button1 = Button(root,text="登录",command=self.login,width=6,height=3,anchor=NE)
        self.button1.pack()
    
        # 照片
        global photo # 把photo声明成全局变量
        photo=PhotoImage(file="./srcs/img.png")
        self.button2 = Button(root,image=photo,command=self.login)
        self.button2.pack()
        #self.button2.config(state="disabled")  # 设置按钮为禁用

    def login(self):
        messagebox.showinfo("message","登录成功")


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x100+500+500")
    root.title("label测试")
    app = Application(master=root)
    root.mainloop()
