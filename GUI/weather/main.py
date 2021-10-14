# 崔浩然
# 时间:2021/9/30 18:36
# 功能:主函数
from tkinter import *
from loginPage import *
if __name__ == "__main__":
    root = Tk()
    root.geometry("300x180+100+200")
    root.title("天气预报查询软件")
    root.resizable(False,False)
    Login(root)           #先启动登录页面，再跳转主界面
    
    root.mainloop()
    