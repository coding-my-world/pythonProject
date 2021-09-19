# 崔浩然
# 时间:2021/8/6 8:49
def calc(a,b): #a,b称为形式参数，简称形参，形参的位置在函数的定义处
    c=a+b
    return c

result=calc(10,20) #10,20为实际参数的值，简称实参，实参的位置在函数的调用处
print(result)

res=calc(b=10,a=20)
print(res)