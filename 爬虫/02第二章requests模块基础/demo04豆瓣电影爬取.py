# 崔浩然
# 时间:2021/9/13 15:57
import json

import requests
if __name__ == '__main__':
    url='https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '1',     #从库中的第几部电影去取
        'limit': '20',     #一次取出的数量
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }
    response=requests.get(url=url,params=param,headers=headers)
    
    list_data = response.json()
    
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    fp.close()
    print('over')