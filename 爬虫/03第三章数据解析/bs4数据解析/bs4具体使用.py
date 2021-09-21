# 崔浩然
# 时间:2021/9/19 9:05
# 功能：bs4的具体使用
from bs4 import BeautifulSoup
if __name__ =='__main__':
    #将本地的html文件加载到该对象中
    fp = open('./text.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    #print(soup.a) #soup.tagName 返回的是html中第一次出现的tagName标签
    #print(soup.find('div')) #soup.find()相当于soup.tagName
    #print(soup.find('div', class_= 'song'))
    #print(soup.find_all('a'))
    #print(soup.select('.tang'))
    print(soup.select('.tang>ul>li>a')[0])
    print(soup.select('.tang>ul a')[0])     #空格表示多个层级，大于号表示一个层级
    print(soup.select('.tang>ul a')[0].text)