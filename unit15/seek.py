# 崔浩然
# 时间:2021/8/8 22:16
file=open('a.txt','r')
file.seek(2)
print(file.read())
print(file.tell())
file.close()