# 崔浩然
# 时间:2021/7/27 9:45
#转义字符
print('hello\nworld')  #\转义功能的首字母 n-->newline 的首字符表示换行

print('hello\tworld') #每四个字符一个\t,不够用空格补齐
print('helloooo\tworld')

print('hello\rworld') #退到行首

print('hello\bworld') #退一格

print('http:\\\\www.baidu.com')

print('老师说：\'大家好\'')

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r，或R
print(r'hello\nworld')

#注意事项：最后一个字符不能是反斜线
