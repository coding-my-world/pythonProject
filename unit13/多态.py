# 崔浩然
# 时间:2021/8/8 9:41
class animal:
    def eat(self):
        print('eat')

class dog(animal):
    def eat(self):
        print('eat gutou')

class cat(animal):
    def eat(self):
        print('eat fish')

class person:
    def eat(obj):
        obj.eat()