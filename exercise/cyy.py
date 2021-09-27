# 崔浩然
# 时间:2021/9/29 16:03
# 功能
def xinjian(): # 新建功能函数
    pass

def xianshi():# 显示全部信息函数
    pass


while True:
    action=input("请输入要选择的功能")
    if action:  #判断是不是为空
        if action == '1':
            print('新建学生信息')
            xinjian()
        elif action =='2':
            print('显示全部信息')
            xianshi()
