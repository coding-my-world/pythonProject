# 崔浩然
# 时间:2021/7/27 9:29
#可以输出数字
print(520)
print(98.5)

#可以输出字符串
print("helloworld")
print('helloworld')

#可以输出含有运算符的表达式
print(3+1)

#将数据输出文件中
fp=open('D:/text.txt','a+')     #如果文件不存在就创建，存在就在文件内容的后面继续追加
print('helloworld',file=fp)
fp.close()

#不进行换行输出（输出内容在一行中）
print('hello','world','python')

