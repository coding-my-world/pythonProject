# 崔浩然
# 时间:2021/8/8 10:17
a=20
b=100
c=a+b
d=a.__add__(b)
print(c)
print(d)

class student:
    def __init__(self,name):
        self.name=name
    def __add__(self,other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)

stu1=student('zhangsan')
stu2=student('lisi')

s=stu1+stu2 #实现了两个对象可以实现加法运算
print(s)
print('-------------')
lst=[11,22,33,44]
print(len(lst))
print(lst.__len__())
print(len(stu1))