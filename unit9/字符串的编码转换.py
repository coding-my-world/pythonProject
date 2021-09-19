# 崔浩然
# 时间:2021/8/5 21:19
s='天涯共此时'
#编码
print(s.encode(encoding='GBK')) #在GBK这种编码中一共中文占两个字节
print(s.encode(encoding='UTF-8')) #在UTF-8这种编码中一共中文占三个字节

#解码
#byte代表的是一个二进制数据（字节类型的数据）
byte=s.encode(encoding='gbk')#编码
print(byte.decode(encoding='gbk'))#解码
#编码和解码的格式要相同
