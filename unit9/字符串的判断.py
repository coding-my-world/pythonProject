# 崔浩然
# 时间:2021/8/4 17:52
s='hello,python'
#判断指定的字符串是不是合法的标识符 (字母数字下划线）
print(s.isidentifier())
#判断指定的字符串是否全部由空白字符组成(回车、换行，水平制表符)
print(s.isspace())
# 判断指定的字符串是否全部由字母组成
print(s.isalpha())
#判断指定字符串是否全部由十进制的数字组成
print(s.isdecimal())
#判断指定的字符串是否全部由数字组成
print(s.isnumeric())
#判断指定字符串是否全部由字母和数字组成
print(s.isalnum())
