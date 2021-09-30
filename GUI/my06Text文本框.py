# 崔浩然
# 时间:2021/9/30 10:26
# 功能：
from tkinter import *
import webbrowser


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()
        
        
    def createWidget(self):
        self.w1 = Text(root,width=40,height=12,bg='gray')
        #宽度20个字母（10个汉字），高度一个行高
        self.w1.pack()
        
        self.w1.insert(1.0,'0123456789\nabcdefg')
        self.w1.insert(2.3,'锄禾日当午，汗滴禾下土。\n')
        
        Button(self,text='重复插入文本',command=self.insertText).pack(side='left')
        Button(self,text='返回文本',command=self.returnText).pack(side='left')
        Button(self,text='添加图片',command=self.addImage).pack(side='left')
        Button(self,text='添加组件',command=self.addWidget).pack(side='left')
        Button(self,text='通过tag精确控制文本',command=self.textTag).pack(side='left')
        
    def insertText(self):
        #insert索引表示在光标处插入
        self.w1.insert(INSERT,'Gaoqi ')
        #END索引号表示在最后插入
        self.w1.insert(END,'[sxt]')
        self.w1.insert(1.8, 'gaoqi')
        
    def returnText(self):
        # Indexes(索引）是用来指向text组件中文本的位置，text的组件索引也是对应实际字符之间的位置
        # 核心；行号从1开始，列号从0开始
        print(self.w1.get(1.2,1.6))
        print('所有文本内容：\n' + self.w1.get(1.0),END)
        
    def addImage(self):
        #global photo
        self.photo = PhotoImage(file= './srcs/img.png')
        self.w1.image_create(END,image = self.photo)
    
    def addWidget(self):
        b1=Button(self.w1,text='点我')
        #在text创建组件命令
        self.w1.window_create(INSERT,window=b1)
        
    # 通过tag精确控制文本
    def textTag(self):
        self.w1.delete(1.0,END)
        self.w1.insert(INSERT,'good good study,day day day up!\n北京尚学堂\n百战程序员\n百度，搜一下')
        self.w1.tag_add('good',1.0,1.9) #选择区域并进行操作
        self.w1.tag_config('good',background='yellow',foreground='red')
        
        self.w1.tag_add("baidu",4.0,4.2)
        self.w1.tag_config('baidu',underline=True)
        self.w1.tag_bind('baidu','<Button-1>',self.webshow)
    
    def webshow(self,event):
        webbrowser.open("http://www.baidu.com")
    
if __name__ == "__main__":
    root = Tk()
    root.geometry("400x200+500+200")
    root.title("label测试")
    app = Application(master=root)
    root.mainloop()