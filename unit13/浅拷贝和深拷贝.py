# 崔浩然
# 时间:2021/8/8 11:34
class cpu:
    pass
class disk:
    pass
class computer:
    def __init__(self,cpu,disk):
        self.disk=disk
        self.cpu=cpu

#(1)变量的赋值
cpu1=cpu()
cpu2=cpu1
print(cpu1)
print(cpu2)

#(2）类的浅拷贝
print('-----------')
disk=disk()
computer=computer(cpu1,disk)
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

#深拷贝
print('-----------------------------------------')
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)