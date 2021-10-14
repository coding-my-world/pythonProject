# 崔浩然
# 时间:2021/10/11 14:38
# 功能


import random
import tkinter as tk


def C_keyin():
    keyin = random.choice(['剪刀', '石頭', '布'])
    return keyin


window = tk.Tk()
window.title("猜拳")
window.geometry('600x600')
l = tk.Label(window, text='來猜拳',
             bg='green', font=('Aria', 48),
             width=15, height=2)
l.pack()
var = tk.StringVar()
var.set("開始吧")
l1 = tk.Label(window, textvariable=var,
              bg='yellow', font=('Aria', 24),
              width=30, height=2)
l1.pack()
on_hit_Cut = on_hit_Rock = on_hit_Paper = False


def btn_Cut():
    global on_hit_Cut
    global p_keyin
    if on_hit_Cut == False:
        on_hit_Cut = True
        p_keyin = "剪刀"
        game()


def btn_Rock():
    global on_hit_Rock
    global p_keyin
    if on_hit_Cut == False:
        on_hit_Cut = True
        p_keyin = "石頭"
        game()


def btn_Paper():
    global on_hit_Paper
    global p_keyin
    if on_hit_Cut == False:
        on_hit_Cut = True
        p_keyin = "布"
        game()


b1 = tk.Button(window, width=15, height=5, command=btn_Cut, text="剪刀").place(x=75, y=300)
b2 = tk.Button(window, width=15, height=5, command=btn_Rock, text="石頭").place(x=225, y=300)
b3 = tk.Button(window, width=15, height=5, command=btn_Paper, text="布").place(x=375, y=300)


def game():
    c_keyin = C_keyin()  # 所以先變成一個變數
    if (p_keyin == c_keyin):
        var.set("你出'%s' 電腦出'%s' 沒輸沒贏喔" % (p_keyin, c_keyin))
    elif ((p_keyin == "剪刀" and c_keyin == "布") or
          (p_keyin == "石頭" and c_keyin == "剪刀") or
          (p_keyin == "布" and c_keyin == "石頭")):
        var.set("你出'%s' 電腦出'%s' 你贏" % (p_keyin, c_keyin))
    else:
        var.set("你出'%s' 電腦出'%s' 你輸" % (p_keyin, c_keyin))


window.mainloop()
