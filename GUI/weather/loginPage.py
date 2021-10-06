# 崔浩然
# 时间:2021/9/30 18:38
# 功能：登录界面
from tkinter import *
from tkinter.messagebox import *
from mainPage import *


class Login(object):
        def __init__(self, master=None):
                self.root = master  # 定义内部变量root
               
                self.username = StringVar()
                self.password = StringVar()
                self.createPage()
        
        def createPage(self):
                self.page = Frame(self.root)  # 创建Frame
                self.page.pack()
                Label(self.page).grid(row=0, stick=W)
                Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
                Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
                Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
                Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
                Button(self.page, text='登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10)
                Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)
                self.username.set('123')
                self.password.set('456')
   
        def loginCheck(self):
                name = self.username.get()
               
                secret = self.password.get()
                
                if name == '123' and secret == '456':
                        self.page.destroy()
                        Main_Page(self.root)
                else:
                        showinfo(title='错误', message='账号或密码错误！')