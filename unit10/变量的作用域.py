# 崔浩然
# 时间:2021/8/6 10:20
def fun3():
    global age   #函数内部定义的变量，局部变量，局部变量使用global声明，就变成了全局变量
    age=3
    print(age)
fun3()
print(age)