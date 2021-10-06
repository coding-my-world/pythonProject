# 崔浩然
# 时间:2021/10/5 8:30
# 功能：扑克牌
from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)  #super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()
    
    def createWidget(self):
        # 通过place布局管理器实现扑克牌位置的控制
        self.photos =[PhotoImage(file="srcs/img.png") for i in range(10)]
        self.pukes =[Label(self.master, image=self.photos[i]) for i in range(10)]
        for i in range(10):
            self.pukes[i].place(x=10 + i * 40, y=50)
        
        
        #为所有的Label增加事件处理
        self.pukes[0].bind_class("Label","<Button-1>",self.chupai)
    def chupai(self,event):
        print(event.widget.winfo_geometry())
        print(event.widget.winfo_y())
        
        if event.widget.winfo_y()==50:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)
            
            
if __name__ == '__main__':
    root = Tk()
    root.geometry("600x270+200+300")
    app=Application(master=root)
    root.mainloop()