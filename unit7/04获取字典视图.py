# 崔浩然
# 时间:2021/8/1 11:01
scores={'张三':100,'李四':98,'王五':45}
#获取所有的key
keys=scores.keys()
print(keys,type(keys))
print(list(keys),type(list(keys)))

#获取所有的value
values=scores.values()
print((values,type(values)))

#获取所有的key-value对
items=scores.items()
print(items,type(items))
print(list(items)) #转化之后的列表元素是由元组组成（元组将在下一个章节讲解）