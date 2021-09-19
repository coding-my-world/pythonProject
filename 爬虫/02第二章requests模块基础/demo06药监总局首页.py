# 崔浩然
# 时间:2021/9/15 16:45
# 功能：
import requests
if __name__== "__main__":
    url='http://scxk.nmpa.gov.cn:81/xk/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }

    page_text = requests.get(url=url,headers=headers).text
    with open('./huazhuangpin.html','w',encoding='utf-8') as fp:
        fp.write(page_text)