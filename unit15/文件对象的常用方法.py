# 崔浩然
# 时间:2021/8/8 22:08
'''read([size])
从文件中读取size个字节或字符的内容返回。若省略[size]，
则读取到文件末尾，即一次读取文件所有内容
readline()
从文本文件中读取一行内容

readlines()
把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回

write(str)
将字符串str内容写入文件

writelines(s_list)
将字符串列表s_list写入文本文件，不添加换行符

seek (offset[, whence])
把文件指针移动到新的位置，offset表示相对于whence的位置:
offset:为正往结束方向移动，为负往开始方向移动
whence不同的值代表不同含义:
0:从文件头开始计算（默认值)
1:从当前位置开始计算
2:从文件尾开始计算

tell()
返回文件指针的当前位置

flush()
把缓冲区的内容写入文件，但不关闭文件

close()
把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关
资源
'''
file=open('c.txt','a')
lst=['java','go','python']
file.writelines(lst)
file.close()