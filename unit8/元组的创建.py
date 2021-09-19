# 崔浩然
# 时间:2021/8/2 9:42
#第一种:使用（）
t=('Python','world',98)
print(t)
print(type(t))

t2='Python','world',98          #省略了小括号
print(t2)
print(type(t2))

t3=('Python',)             #如果元组中只有一个元素，逗号不能省
print(t3)
print(type(t3))

#第二种创建方式，使用tuple（）
t1=tuple('Python','world',98)
print(t1)
print(type(t1))



#空列表创建方式
lst=[]
lst1=list()

#空字典
d={}
d2=dict()

#空元组创建方式
t4=()
t5=tuple()