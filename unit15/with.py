# 崔浩然
# 时间:2021/8/9 8:33
#with语句可以自动管理上下文资源,不论什么原因跳出with块,都能确保文件正确的关闭，以此来达到释放资源的目的
with open('a.txt','r') as file:
    print(file.read())



'''mycontentmgr实现了特殊方法 __enter__()，__exit__（）称为该类对象遵守了上下文管理器协议
该类对象的实例对象，称为上下文管理器'''
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self,exc_type,exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用执行了')

with MyContentMgr() as file1:  #相当于file1=mycontentmgr（）
    file1.show()
