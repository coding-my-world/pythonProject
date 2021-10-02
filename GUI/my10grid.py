# 崔浩然
# 时间:2021/10/1 18:33
# 功能：用grid实现页面布局
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()
    
    def createWidget(self):
        #通过grid实现登录界面
        self.label1 = Label(self,text='用户名')
        self.label1.grid(row=0, column=0)
        self.entry1 =Entry(self)
        self.entry1.grid(row=0,column=1)
        Label(self,text='用户名为手机号').grid(row=0, column=2)
        
        Label(self,text='密码').grid(row=1, column=0)
        Entry(self,text='*').grid(row=1, column=1)
        
        Button(self,text="登录").grid(row= 2, column=1,sticky=EW)
        Button(self,text='取消').grid(row=2, column=2, sticky=E)

if __name__ == "__main__":
    root = Tk()
    root.geometry("400x200+500+200")
    root.title("label测试")
    app = Application(master=root)
    root.mainloop()
