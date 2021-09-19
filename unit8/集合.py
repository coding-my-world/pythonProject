# 崔浩然
# 时间:2021/8/2 11:05

#第一种创建方式使用{}
s={2,3,5,5,7,7,8,9}
print(s)

#第二种创建方式使用set（）
s1=set(range(6))
print(s1,type(s1))
s2=set([1,2,3,4,5,6,7])
print(s2,type(s2))
s3=set(('Python',1,3,5,6))
print(s3,type(s3))
s4=set("Python")
print(s4,type(s4))

s7=set()#定义空集合
下次p72