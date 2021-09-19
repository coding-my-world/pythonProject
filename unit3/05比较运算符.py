# 崔浩然
# 时间:2021/7/29 11:00
#比较运算符
a,b=10,20
print('a>b吗',a>b)
print('a<b吗',a<b)
#a<=b  a>=b a==b a!=b 都是bool类型

'''一个 = 称为赋值运算符， ==称为比较运算符
一个变量由三部分组成：标识，类型，值
==比较的是值
比较对象的标识使用is '''


a=10;
b=10;
print(a==b)  #True 说明a与b的value相等
print(a is b)#True说明a与b的id标识相等
'''python在创建变量时，如果有值为10的对象那么会直接把这个地址给b所以a和b的标识相同'''
lst1=[11,22,33,44]
lst2=[11,22,33,44]

print(lst1==lst2) #value True
print(lst1 is lst2) #id  False
print(id(lst1))
print(id(lst2))

print(a is not b) #False
print(lst1 is not lst2) #True