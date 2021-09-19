# 崔浩然
# 时间:2021/8/6 11:54
try:
    n1=int(input('请输入一个整数:'))
    n2=int(input('请输入另一个整数:'))
    result=n1/n2
    print('结果为:', result)
except ZeroDivisionError :
    print('除数不能为0哦!!!')
except ValueError:
    print('只能输入数字串')

#try--except--else结构
try:
    n1=int(input('请输入一个整数:'))
    n2=int(input('请输入另一个整数:'))

    print('结果为:', result)
except BaseException:
    print('出错了')
else:
    print(n1 / n2)

#try--except---else---finally结构
try:
    n1=int(input('请输入一个整数:'))
    n2=int(input('请输入另一个整数:'))
    result=n1/n2
except BaseException as e :
    print('出错了')
    print(e)
else:
    print('结果为:',result)
finally:
    print('谢谢您的使用')

