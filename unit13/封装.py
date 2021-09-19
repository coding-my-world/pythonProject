# 崔浩然
# 时间:2021/8/6 17:50
class student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #年龄不希望在类的外部被使用，所以加了两个__
    def show(self):
        print(self.name,self.__age)
stu=student('zhangsan',20)
stu.show()
#在类的外部使用name和age
print(stu.name)
#print(stu.__age) #attributeError
#print(dir(stu))

print(stu._student__age) #在类的外部可以通过_student__age访问