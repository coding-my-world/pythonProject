# 崔浩然
# 时间:2021/10/1 17:22
# 功能:canvas画布
import random
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()
    
    def createWidget(self):
        self.canvas = Canvas(self, width=300, height=200,bg = "green")
        self.canvas.pack()
        # 画一条直线 （10，10）（30,20）（40,50）是三个坐标，create_line可以是把他们连起来
        line = self.canvas.create_line(10, 10, 30, 20, 40, 50)
        
        # 画一个矩形·（50，50）是左上角的坐标（100,100）是右下角的坐标
        rect = self.canvas.create_rectangle(50, 50, 100, 100)
        # 画一个椭圆.坐标两双。为椭圆的边界矩形左上角和底部右下角
        oval = self.canvas.create_oval(50, 50, 100, 100)
        
        global photo
        photo = PhotoImage(file="./srcs/img.gif")
        self.canvas.create_image(150, 170, image = photo)
        Button(self, text="画10个矩形", command = self.draw50Recg).pack(side="left")
    
    def draw50Recg(self):
        for i in range(0,10):
            x1=random.randrange(int(self.canvas['width']/2))
            y1=random.randrange(int(self.canvas['height']/2))
            x2=x1+random.randrange(int(self.canvas['width']/2))
            y2=y1+random.randrange(int(self.canvas['height']/2))
            self.canvas.create_rectangle(x1,y1,x2,y2)
if __name__ == "__main__":
    root = Tk()
    root.geometry("400x100+500+500")
    root.title("label测试")
    app = Application(master=root)
    root.mainloop()