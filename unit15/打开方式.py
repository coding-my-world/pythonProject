# 崔浩然
# 时间:2021/8/8 21:58
'''r
以只读模式打开文件，文件的指针将会放在文件的开头
w
以只写模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头
a
以追加模式打开文件，如果文件不存在则创建，文件指针在文件开头，如果文件存在，则在文件末尾追加内容，文件指针在原文件末尾
b
以二进制方式打开文件，不能单独使用，需要与共它模式一起使用，rb，或者wb
+以读写方式打开文件，不能单独使用，需要与其它模式一起使用，a+
'''
file=open('b.txt','w')
file.write('helloworld')
file.close()