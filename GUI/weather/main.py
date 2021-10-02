# 崔浩然
# 时间:2021/9/30 18:36
# 功能:main函数
from tkinter import *

from PIL import Image,ImageTk
from 函数 import *

if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600+100+200")
    root.title("天气预报查询软件")
    root.resizable(False,False)
    app = Application(master=root)
    
    root.mainloop()
