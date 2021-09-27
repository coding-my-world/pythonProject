# 崔浩然
# 时间:2021/9/28 18:41
# 功能：测试label组件的基本用法，使用面向对象的方式
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
        self.label1 = Label(self,text="点我", width=10, height=2, bg="black",fg="white")
        self.label1.pack()
        self.label2 = Label(self,text="点我2", width=10, height=2, bg="blue",fg="white",font=("黑体", 30))
        self.label2.pack()

        # 照片
        global photo # 把photo声明成全局变量
        photo=PhotoImage(file="./srcs/img.png")
        self.label3 = Label(self,image=photo)
        #self.label3.pack()
        self.button4 = Label(self,text="1234",borderwidth=2,relief="ridge",justify= "right")
        self.button4.pack()
        # 创建一个退出按钮
        self.buttonQuit = Button(self, text="退出", command=root.destroy)
        self.buttonQuit.pack()
        Label(root, text="flat", relief="flat").pack()
        Label(root, text="groove", relief="groove").pack()
        Label(root, text="raised", relief="raised").pack()
        Label(root, text="ridge", relief="ridge").pack()
        Label(root, text="solid", relief="solid").pack()
        Label(root, text="sunken", relief="sunken").pack()

    def onclick1(self):
        messagebox.showinfo("message","叫你点你就点?")


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x100+500+500")
    root.title("label测试")
    app = Application(master=root)
    root.mainloop()
