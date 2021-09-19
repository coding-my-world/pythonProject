# 崔浩然
# 时间:2021/9/5 11:26
import os

filename='student.txt'
def main():
    while True:
        menu()
        choice=int(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('您要退出系统吗？y/n')
                if answer=='y'or answer=='Y':
                   print('谢谢您的使用！！！')
                   break
                else:
                    continue
            elif choice ==1:
                insert()# 录入学生信息
            elif choice==2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                 sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menu():
    print('==========================学生信息管理系统===============================')
    print('----------------------------功能菜单------------------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出')
    print('-----------------------------------------------------------------------')
def insert():
    student_list=[]
    while True:
        id=input('请输入id：')
        if not id:
            break
        name=input('请输入姓名：')
        if not name:
            break
        try:
            english=int(input('请输入英语成绩'))
            python=int(input('请输入python成绩'))
            java=int(input('请输入java成绩'))
        except:
            print('不是有效的成绩')
            continue
        #将录入的成绩保存到字典中
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        answer=input('是否继续添加信息y/n\n')
        if answer=='y' or answer=='Y':
            continue
        else:
            break
    #调用save（）函数
    save(student_list)
    print('学生信息录入完毕')
def  save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('id ： name:2')
            if mode=='1':
                id=input('亲输入学生id')
            elif mode=='2':
                name=input('学生姓名：')
            else:
                print("重输")
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id !='':
                        if d['id']==id:
                            student_query.append(d)
                    elif name !='':
                        if d['name']==name:
                            student_query.append(d)
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer=input('是否要继续查询？y\n\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('暂未保存学员信息')
            return
def show_student(lst):
    if len(lst)==0:
        print('查无此人')
        return
    #定义标题格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    #定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int( item.get('python'))+int( item.get('java'))))
def delete():
    while True:
        student_id=input('请输入要删除学生的id：')
        if student_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item)) #将字符串转化成字典
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag==True:
                        print(f'id为{student_id}的学生的信息已经删除')
                    else:
                       print(f'没有找到{student_id}的学生信息')
            else:
                print('没有学生信息')
                break
            show()
            answer=input('是否继续删除？y/n\n')
            if answer=='y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists((filename)):
       with open(filename,'r',encoding='utf-8') as rfile:
         student_old=rfile.readlines()
    else:
       return
    student_id=input('请输入要修改的学员的id：')
    with open(filename,'w',encoding='utf-8')as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id']==student_old:
                print('找到学生信息，可以修改他的相关信息了！')
                while True:
                    try:
                        d['name'] = input('请输入姓名')
                        d['english'] = input('english')
                        d['python'] = input('python')
                        d['java'] = input('java')
                    except:
                        print('输错了')
                        
                wfile.write(str(d)+'\n')
                print('修改成功')
            else:
                wfile.write(str(d)+'\n')
            answer=input('是否继续修改其他学生信息?y/n\n')
            if answer=='y':
                modify()
def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_lst=rfile.readlines()
        student_new=[]
        for item in student_lst:
            d=dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc=input('亲选择0.升序1.降序：')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
        pass
    else:
        sort()
    mode=input('选择按什么排序（1。英语2.python，3.java 0.总成绩：）')
    if mode=='1':
        student_new.sort(key=lambda student_new:int(student_new['english']),reverse=asc_or_desc_bool)
    elif mode=='2':
        student_new.sort(key=lambda student_new:int(student_new['python']),reverse=asc_or_desc_bool)
    elif mode=='3':
        student_new.sort(key=lambda student_new:int(student_new['java']),reverse=asc_or_desc_bool)
    elif mode=='0':
        student_new.sort(key=lambda student_new:int(student_new['english'])+int(student_new['java'])+int(student_new['python']),reverse=asc_or_desc_bool)
    else:
        print('重新输入')
        sort()
    show_student(student_new)
def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            if students:
                print('一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据')
def show():
    student_lst=[]
    if os.path.exists((filename)):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存信息')
if __name__=='__main__':
    main()
