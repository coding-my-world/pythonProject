# 崔浩然
# 时间:2021/8/4 7:25
s={10,20,30,40,50}

#集合元素的判断操作
print(10 in s)
print(100 in s)

#集合元素的新增操作
s.add(80)
print(s)
s.update([100,99,8])
s.update((78,64,65))
print(s)

#集合元素删除操作
s.remove(100)
print(s)
#s.remove(500) keyError:500
s.discard(500)  #元素不存在不抛出异常
s.pop() #随机删除一个元素
print(s)
s.clear() #清空集合
