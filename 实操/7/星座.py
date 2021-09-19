#星座列表
constellation=['asd','qwe']

#性格列表
nature=['asdf','sdfg']

#将两个列表转化成集合
d=dict(zip(constellation,nature))
print(d)
key=input('shuru')
flag=True
for item in d:
    if key==item:
        print(key,'的性格特点为：',d.get(key))
        break
    else:
        flag=False

if not flag:
    print('对不起，输错了')
    