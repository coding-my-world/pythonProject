# 崔浩然
# 时间:2021/10/5 8:14
# 功能
from tkinter import *
root = Tk()
root.geometry("500x300")
root.title="place布局管理器"
root["bg"]="white"
f1 = Frame(root,width=200,height=200,bg="green")
f1.place(x=20,y=30)
Button(root,text="尚学堂").place(relx=0.2,x=100,y=20,relwidth=0.2,relheight=0.5) #relwidth是相对宽度
Button(root,text="百战程序员").place(relx=0.6,rely=0.7)
Button(root,text="崔浩然nb").place(relx=0.5,rely=0.2)
root.mainloop()