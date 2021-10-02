# 崔浩然
# 时间:2021/9/30 18:38
# 功能：存放各个执行函数的代码
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
class Application(Frame):

        def createWidget(Frame):
                # 创建登录界面的组件
                Frame.label01 = Label(Frame, text='用户名')
                Frame.label01.pack()

                # StringVar变量绑定到指定的组件
                # StringVar变量的值发生变化，组件内容也变化
                # 组件内容发生变化，StringVar变量的值发生变化
                v1 = StringVar()
                self.entry01 = Entry(self, textvariable=v1)
                self.entry01.pack()

                print(v1.get())
                print(self.entry01.get())

                # 创建密码框
                self.label02 = Label(self, text="密码")
                self.label02.pack()

                v2 = StringVar()
                self.entry02 = Entry(self, textvariable=v2, show='*')
                self.entry02.pack()

                Button(self, text="登陆", command=self.login).pack()
        #登录函数
        def login(self):
                print("用户名：" + self.entry01.get())
                print("密码：" + self.entry02.get())
                messagebox.showinfo("message", "登录成功")


        #打开指定的图片文件，缩放至指定尺寸

        def bground(self,root):
                image2 = Image.open('./srcs/img.gif')
                background_image = ImageTk.PhotoImage(image2)


                background_label = Label(root, image=background_image)
                background_label.place(x=0, y=0, relwidth=1, relheight=1)
                self.canvas_root.pack()
