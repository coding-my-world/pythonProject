# 崔浩然
# 时间:2021/8/6 10:04
def fun(*args): #函数定义时的可变的位置参数
    print(args)
    print(args[0])

fun(10)
fun(10,20)
fun(10,20,30)

def fun1(**args):
    print(args)

fun1(a=10)
fun1(a=20,b=30,c=40)