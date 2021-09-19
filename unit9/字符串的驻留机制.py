# 崔浩然
# 时间:2021/8/4 9:44
a='Python'
b='Python'
c='Python'
print(id(a))
print(id(b))
print(id(c))
s1='%'
s2='%'
print(s1==s2)
print(s1 is s2)

s1='abc%'
s2='abc%'
print(id(s1))
print(id(s2))
print(s1==s2)
print(s1 is s2)

s1='abcx'
s2='abcx'
print(s1==s2)
print(s1 is s2)

