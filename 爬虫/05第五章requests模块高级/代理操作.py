# 崔浩然
# 时间:2021/9/24 18:46
# 功能：代理操作
import requests
url='https://ip.cn/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }
page_text=requests.get(url=url,headers=headers,proxies={'http//':'43.243.166.222'}).text
with open('./ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)