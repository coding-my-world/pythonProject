# 崔浩然
# 时间:2021/10/5 19:48
# 功能：主界面
from tkinter import *
from tkinter import messagebox
from city_weather import *

class Main_Page(object):
    def __init__(self, master=None):
        self.root=master
        self.root.geometry('300x100')
        self.createWidget()
    
    def createWidget(self):
        # 创建搜索城市框
        self.label01 = Label(self.root, text='输入要查询天气的城市：')
        self.label01.pack()
        
       
        v1 = StringVar()
        self.entry01 = Entry(self.root, textvariable=v1)
        self.entry01.pack()
        #tkinter要求由按钮（或者其它的插件）触发的控制器函数不能含有参数
        Button(self.root,text="查询",command= lambda : self.tianqi(self.entry01.get())).pack()
        
    def tianqi(self,name):
        weather=get_weather(name)
       
        str=''
        for i in weather:
            str=str+i.get("title")
            str=str+":"
            str=str+i.get("text")
            str=str+'\n'
        print(str)
        messagebox.showinfo("%s七天的天气"%name, str)
    
    
    
