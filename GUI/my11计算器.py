# 崔浩然
# 时间:2021/9/29 11:33
# 功能：计算机软件界面的设计
from tkinter import *
from tkinter import messagebox
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()
    def createWidget(self):
       # 通过grid布局实现计算器的界面
        btnText = (("MC","M+","M-","MR"),
                   ("C", "±" ,"/", "×"),
                   (7, 8, 9, "-"),
                   (4, 5, 6, "+"),
                   (1, 2, 3, "="),
                   (0,   "."    ))
        Entry(self).grid(row=0, column=0, columnspan=4, pady=10)
        
        for rindex, r in enumerate(btnText):
            for cindex,c in enumerate(r):
                if c=="=":
                    Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex, rowspan=2, sticky=NSEW)
                elif c==0:
                    Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex, columnspan=2, sticky=NSEW)
                elif c==".":
                    Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex+1, sticky=NSEW)
                else:
                    Button(self, text=c, width=2).grid(row=rindex+1,column=cindex,sticky=NSEW)
    
if __name__ == "__main__":
    root = Tk()
    root.geometry("200x220+500+500")
    root.title("计算器")
    app = Application(master=root)
    root.mainloop()
