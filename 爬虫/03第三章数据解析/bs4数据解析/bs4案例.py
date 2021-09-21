# 崔浩然
# 时间:2021/9/19 10:10
# 功能：bs4实战案例
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    url="https://www.shicimingju.com/book/sanguoyanyi.html"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }
    page_text = requests.get(url=url,headers=headers).content
    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url ='http://www.shicimingju.com'+li.a['href']
        print(detail_url)
        detail_page_text=requests.get(url=detail_url,headers=headers).content

        #解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        #解析到章节的内容
        content = div_tag.text
        fp.write(title+':'+content+'\n')

    fp.close()
    print('over')