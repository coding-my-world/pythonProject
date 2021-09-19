# 崔浩然
# 时间:2021/8/4 18:13
s='hello,python'
#replace()
#第1个参数指定被替换的子串，第2个参数指定替换子串的字符串,该方法返回替换后得到的字符串，
# 替换前的字符串不发生变化,调用该方法时可以通过第3个参数指定最大替换次数
print(s.replace('python','Java'))
s1='hello,Python,Python,Python'
print(s1.replace('Python','Java',2))
#将列表或元组中的字符串合并成一个字符串
lst=['hello','java','Python']
print('|'.join(lst))
print(''.join(lst))

t=('hello',"java",'python')
print(''.join(t))
print('*'.join('python'))

