# 崔浩然
# 时间:2021/8/8 8:42
class person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class student(person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):
        super(student, self).info()
        print(self.stu_no)

class teacher(person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear

stu=student('张三',20,'2001')
teacher=teacher('李四',34,10)
stu.info()
teacher.info()
