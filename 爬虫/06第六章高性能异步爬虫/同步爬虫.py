# 崔浩然
# 时间:2021/9/25 8:47
# 功能：同步爬虫
import requests
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }
urls={
    'https://i1.hdslb.com/bfs/face/7502ae77a1a0245e71a8763513c2ac9ab478430f.jpg@38w_39h_1c_100q.webp',
    'https://i0.hdslb.com/bfs/sycp/creative_img/202109/c1e5c80968e680e4bbce5850751b5074.jpg@880w_388h_1c_95q',
    'https://i0.hdslb.com/bfs/feed-admin/d6344912810082e3f8bca71bbc80003a52f2bd43.jpg@880w_388h_1c_95q'

}

#获取响应数据的函数
def get_content(url):
    print('正在爬取：',url)
    response=requests.get(url=url,headers=headers)
    if response.status_code==200:
        return response.content

def parse_content(content):
    print('响应数据的长度为：',len(content))
    
for url in urls:
    content=get_content(url)
    parse_content(content)