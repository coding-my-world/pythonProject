# 崔浩然
# 时间:2021/8/8 9:06
# 崔浩然
# 时间:2021/8/8 8:42
class student:
    pass
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0}，我的年龄是{1}'.format(self.name,self.age)



stu=student('zhangsan',20)
print(dir(stu))
print(stu)
print(type(stu))