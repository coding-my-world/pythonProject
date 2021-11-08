# 崔浩然
# 时间:2021/10/20 15:40
# 功能
from selenium import webdriver
from time import sleep
import os
from lxml import etree
import requests
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
    }
if not os.path.exists('./picLibs'):
    os.mkdir('./picLibs')
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get( 'http://demo.mxyhn.xyz:8020/cssthemes6/1.03ZF26/Index.html')
page_text=bro.page_source
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@class="m"]/li |//ul[@class="m2"]/li')
sleep(2)
for li in li_list:
    img_name = li.xpath('./@style')[0]
    src = img_name.split('"')[1]
    img_name = src.split('/')[1]
    src = "http://demo.mxyhn.xyz:8020/cssthemes6/1.03ZF26/" + src
    
    # 存储图片
    img_data = requests.get(url=src, headers=headers).content
    img_path = './picLibs/' + img_name
    print(img_path)
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name, '下载成功!!!')