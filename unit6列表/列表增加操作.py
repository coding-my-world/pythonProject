# 崔浩然
# 时间:2021/8/1 7:34

#向列表的末尾添加一个元素
lst=[10,20,30]
print('添加元素之前',lst,id(lst))
lst.append(100)
print('添加元素之后',lst,id(lst))

lst2=['hello','world']
lst.append(lst2)
print(lst)

#向列表末尾一次性添加多个元素
lst.extend(lst2)
print(lst)

lst3=[True,False,'hello']
#在任意位置上添加N多个元素
lst[1:]=lst3
print(lst)