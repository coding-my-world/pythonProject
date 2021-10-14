# 崔浩然
# 时间:2021/10/8 14:00
# 功能
import tkinter
import math
import decimal
import cmath

result = symbol = None


class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.minsize(260, 400)
        self.root.title('计算器')
        standard(self.root)


class standard():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.standard = tkinter.Frame(self.master, relief=tkinter.RAISED, borderwidth=2)
        self.standard.pack(fill=tkinter.BOTH, expand=1)
        entry1 = tkinter.Label(self.standard, width=40, height=6, bg='white', anchor='se', textvariable=var_text)
        entry1.grid(row=1, columnspan=5)
        # 第一行
        mod_ = tkinter.Button(self.standard, text='%', height=4, width=6, command=lambda: calculate('%'))
        mod_.grid(row=2, column=0)
        SetZero_ = tkinter.Button(self.standard, text='C', height=4, width=6, command=lambda: clear())
        SetZero_.grid(row=2, column=1)
        SetZero_.config(bg='light green')
        delete_ = tkinter.Button(self.standard, text='←', height=4, width=6, command=lambda: del_())
        delete_.grid(row=2, column=2)
        divide_ = tkinter.Button(self.standard, text='÷', height=4, width=6, command=lambda: calculate('÷'))
        divide_.grid(row=2, column=3)
        # 第二行
        number7_ = tkinter.Button(self.standard, text='7', height=4, width=6, command=lambda: press('7'))
        number7_.grid(row=3, column=0)
        number8_ = tkinter.Button(self.standard, text='8', height=4, width=6, command=lambda: press('8'))
        number8_.grid(row=3, column=1)
        number9_ = tkinter.Button(self.standard, text='9', height=4, width=6, command=lambda: press('9'))
        number9_.grid(row=3, column=2)
        multiply_ = tkinter.Button(self.standard, text='×', height=4, width=6, command=lambda: calculate('×'))
        multiply_.grid(row=3, column=3)
        # 第三行
        number4_ = tkinter.Button(self.standard, text='4', height=4, width=6, command=lambda: press('4'))
        number4_.grid(row=4, column=0)
        number5_ = tkinter.Button(self.standard, text='5', height=4, width=6, command=lambda: press('5'))
        number5_.grid(row=4, column=1)
        number6_ = tkinter.Button(self.standard, text='6', height=4, width=6, command=lambda: press('6'))
        number6_.grid(row=4, column=2)
        subtract_ = tkinter.Button(self.standard, text='—', height=4, width=6, command=lambda: calculate('—'))
        subtract_.grid(row=4, column=3)
        # 第四行
        number1_ = tkinter.Button(self.standard, text='1', height=4, width=6, command=lambda: press('1'))
        number1_.grid(row=5, column=0)
        number2_ = tkinter.Button(self.standard, text='2', height=4, width=6, command=lambda: press('2'))
        number2_.grid(row=5, column=1)
        number3_ = tkinter.Button(self.standard, text='3', height=4, width=6, command=lambda: press('3'))
        number3_.grid(row=5, column=2)
        add_ = tkinter.Button(self.standard, text='+', height=4, width=6, command=lambda: calculate('+'))
        add_.grid(row=5, column=3)
        # 第五行
       
        number0_ = tkinter.Button(self.standard, text='0', height=4, width=6, command=lambda: press('0'))
        number0_.grid(row=6, column=1)
        decimal_point_ = tkinter.Button(self.standard, text='.', height=4, width=6, command=lambda: point())
        decimal_point_.grid(row=6, column=2)
        equalnum_ = tkinter.Button(self.standard, text='=', height=4, width=6, command=lambda: calculate('='))
        equalnum_.grid(row=6, column=3)
    
    

# 按下数字
def press(key_):
    print('press', key_)
    if key_ == '.':
        if save.count('.') >= 1:
            pass
        else:
            if save == []:
                save.append('0')
            else:
                save.append(key_)
                var_text.set(''.join(save))
    else:
        save.append(key_)
        var_text.set(''.join(save))


# 删除数字
def del_():
    print("del_")
    if save:
        save.pop()
    else:
        pass
    var_text.set(''.join(save))


# 清空
def clear():
    print("clear")
    save.clear()
    var_text.set(0)


# 运算符函数
def calculate(key_):
    global save, var_text, result, symbol
    if var_text.get() == '':
        pass
    else:
        get1 = decimal.Decimal(var_text.get())
        
       
        if key_ in ('+', '—', '×', '÷', '=', '%', 'log'):
            if symbol is not None:
                get1 = decimal.Decimal(result)
                get2 = decimal.Decimal(var_text.get())
                if symbol == '+':
                    result = get1 + get2
                elif symbol == '—':
                    result = get1 - get2
                elif symbol == '×':
                    result = get1 * get2
                elif symbol == '÷':
                    result = get1 / get2
                elif symbol == '%':
                    result = get1 % get2
                elif symbol == 'log':
                    result = math.log(get2, get1)
                
            else:
                result = get1
            if key_ == '=':
                print('calculate result = ', result)
                symbol = None
            else:
                symbol = key_
                print(symbol)
        var_text.set(str(result))
        save.clear()


# 小数点
def point():
    print('point')
    
    if save.count('.') >= 1:
        pass
    
    else:
        
        if save == []:
            save.append('0')
        
        save.append('.')
        
        var_text.set(''.join(save))


root = tkinter.Tk()
var_text = tkinter.StringVar()
var_text.set(0)
save = []  # -------------------------------存储数字 符号
basedesk(root)
root.mainloop()
