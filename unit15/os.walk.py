# 崔浩然
# 时间:2021/8/9 10:23
import os
path=os.getcwd()
lst_files=os.walk(path)
for dirpath,dirname,filename in lst_files:
    print(dirpath,'dirpath')
    print(dirname,'dirname')
    print(filename,'filename')
    print('-----------------')