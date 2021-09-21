# 崔浩然
# 时间:2021/9/21 11:30
# 功能：爬取58二手房中的房源信息
import requests
from lxml import etree
if __name__ == '__main__':
    url = 'https://qqhr.58.com/ershoufang/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
    }
    #爬取页面源码数据
    page_text = requests.get(url = url,headers=headers).text
    #print(page_text)
    #数据解析
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//section[@class="list"]/div')
    fp = open('58.txt','w',encoding='utf-8')
    for div in div_list:
        title = div.xpath('.//div[@class="property-content-title"]/h3/text()')[0]
        fp.write(title+'\n')
    fp.close()
