# 崔浩然
# 时间:2021/8/4 16:51
#字符串的查找操作
s='hello,hello'
print(s.index('lo')) #3
print(s.find('lo')) #3
print(s.rindex('lo')) #9
print(s.rfind('lo')) #9

#print(s.index('k')) #ValueError:substring not found
print(s.find('k')) #-1
print(s.rindex('k'))#ValueError:substring not found
print(s.rfind('k')) #-1
