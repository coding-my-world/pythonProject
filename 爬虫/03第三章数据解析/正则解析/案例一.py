# 崔浩然
# 时间:2021/9/17 21:40
# 功能：爬取爬取糗事百科中糗图板块下所有的糗图图片
import requests
import re
import os

if __name__ == '__main__':
    
    #创建一个文件夹，保存所有的图片
    if not os.path.exists('../qiutulibs'):
        os.makedirs('../qiutulibs')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }
    
    #设计一个通用的url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d'
    for pageNum in range(1,36):
        #对应页码的url
        new_url = format(url%pageNum)
        #使用通用爬虫对url对应的一整张页面进行爬取
        page_text = requests.get(url=new_url,headers=headers).text
    
        #使用聚焦爬虫将页面中所有的糗图进行解析/提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex,page_text,re.S)
        #print(img_src_list)
        for src in img_src_list:
            #拼接出一个完整的图片url
            src = 'https:'+src
            #请求到了图片的二进制数据
            img_data = requests.get(url=src,headers=headers).content
            
            #生成图片名称
            img_name = src.split('/')[-1]
            
            #图片存储的路径
            imgPath = './qiutulibs/' + img_name
            with open(imgPath,'wb') as fp:
                fp.write(img_data)
                print(img_name,'下载成功！')