# 崔浩然
# 时间:2021/8/9 10:10
#列出指定目录下1所有py文件
import os
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)
