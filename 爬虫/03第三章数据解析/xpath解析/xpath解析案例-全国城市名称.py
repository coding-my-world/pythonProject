# 崔浩然
# 时间:2021/9/21 19:17
# 功能：爬取全国城市名称
import requests
from lxml import etree
if __name__=='__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
    }
    page_text = requests.get(url=url,headers=headers).text
    #加载一个etree对象
    tree=etree.HTML(page_text)
    all_city_name=[]
    #先获取到热门城市的列表再进行一次xpath解析得到热门城市的具体内容
    hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    for li in hot_li_list:
        hot_name=li.xpath('./a/text()')[0]
        all_city_name.append(hot_name)
        
    city_name_list=tree.xpath('//div[@class="bottom"]//div[2]/li')
    for li in city_name_list:
        city_name=li.xpath('./a/text()')[0]
        all_city_name.append(city_name)
    i=0
    i=int(i)
    with open('all_city.txt','w',encoding='utf-8') as fp:
        for i in all_city_name:
            fp.write(i+'\n')
            