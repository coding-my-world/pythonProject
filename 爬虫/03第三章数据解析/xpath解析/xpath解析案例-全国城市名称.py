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
