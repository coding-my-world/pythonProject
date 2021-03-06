# 崔浩然
# 时间:2021/9/29 16:41
# 功能:登录界面设计和实现
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()
    
    def createWidget(self):
        # 创建登录界面的组件
        self.label01 = Label(self,text='用户名')
        self.label01.pack()
        
        # StringVar变量绑定到指定的组件
        # StringVar变量的值发生变化，组件内容也变化
        # 组件内容发生变化，StringVar变量的值发生变化
        v1 = StringVar()
        self.entry01 = Entry(self,textvariable=v1)
        self.entry01.pack()
        v1.set('admin') #将输入框的初始值设为admin
        print(v1.get())
        print(self.entry01.get())
        
        #创建密码框
        self.label02 = Label(self,text="密码")
        self.label02.pack()
        
        v2 = StringVar()
        self.entry02=Entry(self,textvariable=v2,show='*')
        self.entry02.pack()
        
        Button(self,text="登陆",command=self.login).pack()
        
    def login(self):
        print("用户名：" + self.entry01.get())
        print("密码：" + self.entry02.get())
        messagebox.showinfo("message", "登录成功")


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x200+500+200")
    root.title("label测试")
    app = Application(master=root)
    root.mainloop()
