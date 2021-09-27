# 崔浩然
# 时间:2021/8/1 10:28
scores={'张三':100,'李四':98,'王五':45}
'''第一种方式 ，使用【】'''
print(scores['张三'])
#print(scores['陈六']) #keyError：‘陈六’

#第二种方式，使用get（）方法
print(scores.get('张三'))
print(scores.get('陈六'))
print(scores.get('陈六',99))