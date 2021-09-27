# 崔浩然
# 时间:2021/9/27 15:54
# 功能：测试一个经典的GUI程序的写法，使用面向对象的方式
from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)      # super代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()
        
    def createWidget(self): # 创建组件
        self.button1 = Button(self)
        self.button1["text"] = '点我'
        self.button1.pack()
        self.button1["command"]=self.onclick1
        
        #创建一个退出按钮
        self.buttonQuit = Button(self,text="退出",command=root.destroy)
        self.buttonQuit.pack()
    
    def onclick1(self):
        messagebox.showinfo("message","叫你点你就点?")

if __name__ =="__main__":
    root = Tk()
    root.geometry("400x100+200+300")
    root.title("一个经典的GUI程序类的测试")
    app =Application(master=root)
    root.mainloop()