# 崔浩然
# 时间:2021/8/1 8:10
lst=[10,20,30,40,50,60,30]
lst.remove(30) #从列表中移除一个元素，如果有重复元素你们只移除一个元素
print(lst)
#lst.remove(100) #Value Error: list.remove(x):x not in list

#pop() 根据索引移除元素
lst.pop(1)
print(lst)
#lst.pop(5) #IndexError: pop index out of range 如果指定索引位置不存在，将抛出异常
lst.pop() #如果不知道参数（索引），将删除列表中的最后一个元素
print(lst)

print('-----------切片操作-删除至少一个元素，将产生一个新的列表对象----------')
lst4=lst[1:3]
print('原列表',lst)
print('切片后的列表',lst4)

'''不产生新的列表对象，而是删除原列表中的内容'''
lst[1:3]=[]
print(lst)

#清除列表中的所有元素
lst.clear()
print(lst)

#del语句将列表对象删除
del(lst)
#print(lst) #NameError: name 'lst' is not defined