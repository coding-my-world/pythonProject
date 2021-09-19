# 崔浩然
# 时间:2021/8/8 9:58
class a:
    pass
class b:
    pass
class c(a,b):
    def __init__(self,name,age):
        self.name=name
        self.age=age

#创建c类的对象
x=c('jack',20)
print(x.__dict__)
print(c.__dict__)
print('--------------')
print(x.__class__) #<class '__main__.c>输出了对象所属的类
print(c.__bases__) #c类的父类的元素
print(c.__base__) #最近的父类，谁写在前面输出谁
print(c.__mro__) #类的层次结构
print(a.__subclasses__())  #子类的列表
