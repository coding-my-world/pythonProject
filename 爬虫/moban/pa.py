# 崔浩然
# 时间:2021/10/20 10:49

import requests
from lxml import etree
import os

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
    }
    start_url='http://demo.mxyhn.xyz:8020/cssthemes6/1.03ZF26/Index.html'
    
    page_text = requests.get(url=start_url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="m"]/li |//ul[@class="m2"]/li')
    
    # 创建一个文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    for li in li_list:
        img_name = li.xpath('./@style')[0]
        src=img_name.split("(")[1]
        src=src.split(")")[0]
        img_name=src.split('/')[1]
        print(src)
        src="http://demo.mxyhn.xyz:8020/cssthemes6/1.03ZF26/"+src

        # 存储图片
        img_data = requests.get(url=src, headers=headers).content
        img_path = './picLibs/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功!!!')


