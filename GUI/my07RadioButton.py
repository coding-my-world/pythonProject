# 崔浩然
# 时间:2021/10/1 16:36
# 功能
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()
    
    def createWidget(self):
        self.v=StringVar()
        self.v.set('F')
        
        self.r1 = Radiobutton(self,text = '男性',value = 'M', variable=self.v)
        self.r2 = Radiobutton(self,text = '女性',value = 'F', variable=self.v)
    
        self.r1.pack(side = 'left');self.r2.pack(side = 'left')
        
        Button(self,text='确定',command=self.confirm).pack(side = 'left')
        
    def confirm(self):
        messagebox.showinfo('测试','选择的性别：'+ self.v.text())
       


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x100+500+500")
    root.title("label测试")
    app = Application(master=root)
    root.mainloop()