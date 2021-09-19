# 崔浩然
# 时间:2021/7/29 16:05
#range()的三种创建方式
'''第一种创建方式，只有一个参数（小括号中只给一个数）'''
r=range(10)
print(r) #range(0,10)
print(list(r)) #用于查看range对象中的整数序列   -->list是列表的意思

'''第二种创建方式，给了两个参数（小括号中给了两个数）'''
r=range(1,10)     #指定了起始值，从1开始到10结束，不包含10，默认步长为1
print(list(r))    #[1,2,3,4,5,6,7,8,9]

#第三种创建方式，给了三个参数（小括号有三个数），，，
r=range(1,10,2)
print(list(r))  #[1,3,5,7,9]

'''判断指定的整数在序列中是否存在'''
print(10 in r) #False不在当前r的这个整数序列中
print(9 in r) #True

print(10 not in r) #True
print(9 not in r) #False

