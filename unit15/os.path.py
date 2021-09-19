# 崔浩然
# 时间:2021/8/9 9:34
'''
abspath(path)
用于获取文件或目录的绝对路径

exists(path)
用于判断文件或目录是否存在，如果存在返回True,
否则返回False

join(path, name)
将目录与目录或者文件名拼接起来

splitext()
分离文件名和扩展名

basename(path)
从一个目录中提取文件名

dirname(path)
从一个路径中提取文件路径，不包括文件名

isdir(path)
用于判断是否为路径
'''
import os.path
print(os.path.abspath('os.path.py'))
print(os.path.exists('os.path.py'))
