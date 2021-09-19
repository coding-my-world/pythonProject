# 崔浩然
# 时间:2021/7/29 14:36
#测试对象的布尔值


# print('-------以下对象的布尔值为False--------')
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))         #空列表
print(bool(list()))     #空列表
print(bool(()))         #空元祖
print(bool(tuple()))    #空元祖
print(bool({}))         #空字典
print(bool(dict()))     #空字典
print(bool(set()))      #空集合

print('----------其他对象的布尔值均为True-------------')
print(bool(18))
print(bool(True))
print(bool('helloworld'))