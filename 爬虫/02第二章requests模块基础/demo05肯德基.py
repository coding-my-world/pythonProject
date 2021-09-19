# 崔浩然
# 时间:2021/9/14 7:48
import requests
import json
if __name__=='__main__':
    url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

    kw = input('enter a word:')
    param={
        'cname':'',
        'pid':'',
        'keyword':kw,
        'pageIndex':'1',
        'pageSize':'10',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }
    response = requests.post(url=url,data=param, headers=headers)
    page_text=response.text
    with open('./kfc.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('over')