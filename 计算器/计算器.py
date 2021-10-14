# 崔浩然
# 时间:2021/9/24 19:49
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
        science(self.root)
        
class science():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.science = tkinter.Frame(self.master, relief=tkinter.RAISED, borderwidth=2)
        self.science.pack(fill=tkinter.BOTH, expand=1)
        entry1 = tkinter.Label(self.science, width=40, height=6, bg='white', anchor='se',textvariable=var_text)
        entry1.grid(row=1, columnspan=5)
        # 科学计算器运算符号按钮
        # 第一行
        but1 = tkinter.Button(self.science, text='标准', height=2, width=6, command=self.change1)
        but1.grid(row=0, column=0)
        asin = tkinter.Button(self.science, text='asin', height=2, width=6, command=lambda: calculate('asin'))
        asin.grid(row=2, column=0)
        acos = tkinter.Button(self.science, text='acos', height=2, width=6, command=lambda: calculate('acos'))
        acos.grid(row=2, column=1)
        atan = tkinter.Button(self.science, text='atan', height=2, width=6, command=lambda: calculate('atan'))
        atan.grid(row=2, column=2)
        delete_ = tkinter.Button(self.science, text='←', height=2, width=6, command=lambda: del_())
        delete_.grid(row=2, column=3)
        # 第二行
        exponentiation = tkinter.Button(self.science, text='x^y', height=2, width=6, command=lambda: calculate('x^y'))
        exponentiation.grid(row=3, column=0)
        Pi = tkinter.Button(self.science, text='π', height=2, width=6, command=lambda: calculate('π'))
        Pi.grid(row=3, column=1)
        sqrt = tkinter.Button(self.science, text='√', height=2, width=6, command=lambda: calculate('√'))
        sqrt.grid(row=3, column=2)
        SetZero = tkinter.Button(self.science, text='C', height=2, width=6, command=lambda: clear())
        SetZero.grid(row=3, column=3)
        SetZero.config(bg='light green')
        # 第三行
        e = tkinter.Button(self.science, text='e', height=2, width=6,command=lambda: calculate('e'))
        e.grid(row=4, column=0)
        ln = tkinter.Button(self.science, text='ln', height=2, width=6,command=lambda: calculate('ln'))
        ln.grid(row=4, column=1)
        log_ = tkinter.Button(self.science, text='log', height=2, width=6, command=lambda: calculate('log'))
        log_.grid(row=4, column=2)
        divide = tkinter.Button(self.science, text='÷', height=2, width=6, command=lambda: calculate('÷'))
        divide.grid(row=4, column=3)
        # 第四行
        mod = tkinter.Button(self.science, text='%', height=2, width=6, command=lambda: calculate('%'))
        mod.grid(row=5, column=0)
        sin = tkinter.Button(self.science, text='sin', height=2, width=6, command=lambda: calculate('sin'))
        sin.grid(row=5, column=1)
        cos = tkinter.Button(self.science, text='cos', height=2, width=6, command=lambda: calculate('cos'))
        cos.grid(row=5, column=2)
        tan = tkinter.Button(self.science, text='tan', height=2, width=6, command=lambda: calculate('tan'))
        tan.grid(row=5, column=3)
        # 第五行
        number7 = tkinter.Button(self.science, text='7', height=2, width=6, command=lambda: press('7'))
        number7.grid(row=6, column=0)
        number8 = tkinter.Button(self.science, text='8', height=2, width=6, command=lambda: press('8'))
        number8.grid(row=6, column=1)
        number9 = tkinter.Button(self.science, text='9', height=2, width=6, command=lambda: press('9'))
        number9.grid(row=6, column=2)
        multiply = tkinter.Button(self.science, text='×', height=2, width=6, command=lambda: calculate('×'))
        multiply.grid(row=6, column=3)
        # 第六行
        number4 = tkinter.Button(self.science, text='4', height=2, width=6, command=lambda: press('4'))
        number4.grid(row=7, column=0)
        number5 = tkinter.Button(self.science, text='5', height=2, width=6, command=lambda: press('5'))
        number5.grid(row=7, column=1)
        number6 = tkinter.Button(self.science, text='6', height=2, width=6, command=lambda: press('6'))
        number6.grid(row=7, column=2)
        subtract = tkinter.Button(self.science, text='—', height=2, width=6, command=lambda: calculate('—'))
        subtract.grid(row=7, column=3)
        # 第七行
        number1 = tkinter.Button(self.science, text='1', height=2, width=6, command=lambda: press('1'))
        number1.grid(row=8, column=0)
        number2 = tkinter.Button(self.science, text='2', height=2, width=6, command=lambda: press('2'))
        number2.grid(row=8, column=1)
        number3 = tkinter.Button(self.science, text='3', height=2, width=6, command=lambda: press('3'))
        number3.grid(row=8, column=2)
        add = tkinter.Button(self.science, text='+', height=2, width=6, command=lambda: calculate('+'))
        add.grid(row=8, column=3)
        # 第八行
        factorial = tkinter.Button(self.science, text='n!', height=2, width=6, command=lambda: calculate('n!'))
        factorial.grid(row=9, column=0)
        number0 = tkinter.Button(self.science, text='0', height=2, width=6, command=lambda: press('0'))
        number0.grid(row=9, column=1)
        decimal_point = tkinter.Button(self.science, text='.', height=2, width=6, command=lambda: point())
        decimal_point.grid(row=9, column=2)
        equalnum = tkinter.Button(self.science, text='=', height=2, width=6, command=lambda: calculate('='))
        equalnum.grid(row=9, column=3)

    def change1(self, ):
        self.science.destroy()
        standard(self.master)

class standard():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.standard = tkinter.Frame(self.master, relief=tkinter.RAISED, borderwidth=2)
        self.standard.pack(fill=tkinter.BOTH, expand=1)
        entry1 = tkinter.Label(self.standard, width=40, height=6, bg='white', anchor='se',textvariable=var_text)
        entry1.grid(row=1, columnspan=5)
        # 标准计算器运算符号按钮
        # 第一行
        but1_ = tkinter.Button(self.standard, text='科学', height=2, width=6, command=self.change2)
        but1_.grid(row=0, column=0)
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
        square = tkinter.Button(self.standard, text='x^y', height=4, width=6, command=lambda: calculate('x^y'))
        square.grid(row=6, column=0)
        number0_ = tkinter.Button(self.standard, text='0', height=4, width=6, command=lambda: press('0'))
        number0_.grid(row=6, column=1)
        decimal_point_ = tkinter.Button(self.standard, text='.', height=4, width=6, command=lambda: point())
        decimal_point_.grid(row=6, column=2)
        equalnum_ = tkinter.Button(self.standard, text='=', height=4, width=6, command=lambda: calculate('='))
        equalnum_.grid(row=6, column=3)

    def change2(self, ):
        self.standard.destroy()
        science(self.master)


#按下数字
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
#删除数字
def del_():
    print("del_")
    if save:
        save.pop()
    else:
        pass
    var_text.set(''.join(save))
#清空
def clear():
    print("clear")
    save.clear()
    var_text.set(0)
#运算符函数
def calculate(key_):
    global save, var_text, result, symbol
    if var_text.get() == '':
        pass
    else:
        get1 = decimal.Decimal(var_text.get())

        if key_ in ('asin', 'acos', 'atan', 'sin', 'cos', 'tan', '√', 'n!', 'π','e','ln'):

            if key_ == 'asin':
                result = math.asin(get1)
            elif key_ == 'acos':
                result = math.acos(get1)
            elif key_ == 'atan':
                result = math.atan(get1)
            elif key_ == 'sin':
                result = math.sin(get1)
            elif key_ == 'cos':
                result = math.cos(get1)
            elif key_ == 'tan':
                result = math.tan(get1)
            elif key_ == '√':
                result = math.sqrt(get1)
            elif key_ == 'n!':
                result = math.factorial(get1)
            elif key_ == 'π':
                result = cmath.pi
            elif key_ == 'e':
                result = cmath.e
            elif key_ == 'ln':
                result = math.log1p(get1-1)
        elif key_ in ('+', '—', '×', '÷', '=', '%', 'log', 'x^y'):
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
                elif symbol == 'x^y':
                    result = math.pow(get1, get2)
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
#小数点
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
