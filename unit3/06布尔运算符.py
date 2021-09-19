# 崔浩然
# 时间:2021/7/29 11:36
a,b=1,2
print("---------and并且----------")
print(a==1 and b==2) #True
print(a==1 and b<2) #False
print(a!=1 and b==2) #False
print(a!=1 and b!=2) #False]

print('---------or或者--------------')
print(a==1 or b ==2) #True
print(a==1 or b<2) #True
print(a!=1 or b==2)#True
print(a!=1 or b!=2)#False

print('-------not 对bool类型操作数取反------')
f=True
f1=False
print(not f)
print(not f1)

print('------in 和not in----------')
s='helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)