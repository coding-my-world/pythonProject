# 崔浩然
# 时间:2021/9/18 8:20
# 功能：bs4数据解析
#bs4数据解析的原理：
#1.实例化一个beautifulsoup对象，并且将页面源码数据加载到该对象中
#2.通过调用beautiful对象中相关的属性进行标签定位和数据提取
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    #将本地的html文档中的数据加载到该对象中
    fp = open('../正则解析/huazhuangpin.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    print(soup)
    
    #将互联网上获取的页面源码加载到对象中
    url = 'https://www.baidu.com/'
    # UA伪装:将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }
    response = requests.get(url=url,headers=headers)
    page_text = response.text
    soup1 = BeautifulSoup(page_text,'lxml')
    print(soup1)