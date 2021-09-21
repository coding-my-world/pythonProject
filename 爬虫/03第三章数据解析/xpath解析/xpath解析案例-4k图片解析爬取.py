# 崔浩然
# 时间:2021/9/21 18:18
# 功能：解析下载图片数据
import requests
from lxml import etree
import os
if __name__ =='__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
    }
    url ='http://pic.netbian.com/4kmeinv/'
    page_text = requests.get(url=url,headers=headers).text
    tree=etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="clearfix"]/li')
    
    #创建一个文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    for li in li_list:
        img_src='http://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
        img_name=li.xpath('./a/img/@alt')[0]+'.jpg'
        
        #通用处理中文乱码的解决方案
        img_name=img_name.encode('iso-8859-1').decode('gbk')
        
        #存储图片
        img_data=requests.get(url=img_src,headers=headers).content
        img_path='picLibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功!!!')
    
