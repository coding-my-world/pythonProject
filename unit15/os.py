# 崔浩然
# 时间:2021/8/9 9:14
#os模块于操作系统相关的一个模块
'''getcwd()
返回当前的工作目录

listdir(path)
返回指定路径下的文件和目录信息

mkdir(path[, mode])
创建目录

makedirs(path1/path2.. . [, mode])
创建多级目录

rmdir(path)
删除目录

removedirs(path1/path2.. . .. .)
删除多级目录

chdir(path)
将path设置为当前工作目录
'''
import os
#os.system('notepad.exe')
#os.system('calc.exe')

#直接调用可执行文件
#os.startfile('C:\\Users\\ASUS\\Desktop\\程序\\Dev-C++')
print(os.getcwd())
lst=os.listdir('../unit15')
print(lst)
'''
os.mkdir('newdir2’)
os.makedirs('A/B/C')
os.rmdir('newdir2')
os.removedirs('A/B/C')
os.chdir('E:\\vippython\\chap15')
print(os.getcwd())
'''