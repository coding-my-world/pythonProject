# 崔浩然
# 时间:2021/8/6 17:10
class student:
    native_pace='吉林'

    #初始化方法
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #实例方法
    def eat(self):
        print('学生在吃饭...')

    #静态方法
    @staticmethod
    def method():
        print('我使用staticmethod进行修饰，所以我是静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('类方法')
    #在1类之外定义的称为函数，在类之内定义的称为方法
def drink():
    print('喝水')

#类属性的使用方式
print(student.native_pace)
stu1=student('张三',20)
stu2=student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
student.native_pace='天津'
print(stu1.native_pace)
print(stu2.native_pace)

print('----------类方法的使用方式----------')
student.cm()

print('---------静态方法的使用方式----------')


student.method()