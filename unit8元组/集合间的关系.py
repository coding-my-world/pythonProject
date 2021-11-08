# 崔浩然
# 时间:2021/8/4 7:44
s={10,20,30,40}
s2={40,30,20,10}

print(s==s2)

#一个集合是否是另一个集合的子集
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
print(s.issubset(s1))
print(s3.issubset(s1))

#一个集合是否是另一个集合的超集
print(s1.issuperset(s2))
print(s1.issuperset(s3))

#两个集合是否含有交集
print(s2.isdisjoint(s3)) #有交集为false
s4={100,200,300}
print(s2.isdisjoint(s4)) #没交集为true