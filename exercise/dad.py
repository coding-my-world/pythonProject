# 崔浩然
# 时间:2021/9/17 22:52
# 功能
import requests
import re
import os

if __name__ == '__main__':
    
   
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }
    url = 'https://www.qiushibaike.com/imgrank/'

    # 使用通用爬虫对url对应的一整张页面进行爬取
    page_text = requests.get(url=url, headers=headers).text

    # 使用聚焦爬虫将页面中所有的糗图进行解析/提取
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)
    # print(img_src_list)
    for src in img_src_list:
        # 拼接出一个完整的图片url
        src = 'https:' + src
        # 请求到了图片的二进制数据
        img_data = requests.get(url=src, headers=headers).content

        # 生成图片名称
        img_name = src.split('/')[-1]
        print(img_name)
        