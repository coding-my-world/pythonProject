# 崔浩然
# 时间:2021/8/6 18:08
class Person(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name, self.age))
#定义子类
class student (Person):
    def __init__(self, name, age,score):
        super().__init__(name,age)
        self.score=score
#测试
stu=student('Jack',20, '1001')
stu.info()
print(stu.score)
