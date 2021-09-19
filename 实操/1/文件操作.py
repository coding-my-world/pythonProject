# 崔浩然
# 时间:2021/8/12 9:43
'''使用print方式进行输出（输出的目的地是文件）'''
fp=open('test.txt','w')
print('奋斗。。。。。',file=fp)
fp.close()

'''第二种操作，用文件的读写操作'''
with open('test2.txt','w') as file:
    file.write('奋斗。。。。 ')