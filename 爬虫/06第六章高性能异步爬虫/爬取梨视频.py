# 崔浩然
# 时间:2021/9/25 9:37
# 功能：爬取梨视频
import requests
from multiprocessing.dummy import Pool
from lxml import etree
import os
#创建文件夹来单独存放视频
if not os.path.exists('./picLibs'):
    os.mkdir('./picLibs')
page_url='https://www.pearvideo.com/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }

#获取到首页的源码
page_text=requests.get(url=page_url,headers=headers).text

tree=etree.HTML(page_text)
liList=tree.xpath('//div[@id="actwapSlide"]/ul/li')
urls=[] #用来存放视频地址和名称的列表


for li in liList:
    #通过一系列的拼接操作来获取真实地址
    href=li.xpath('./a/@href')[0]
    videohref=page_url+href
    src_list=videohref.split('/')[3]
    true_videotitle=src_list.split('_')[1] #一串数字作为视频的名称，并且存放具有第一种特征数字的字符串
    #在headers里加入防盗链，不然无法获取到存放间接地址的json数据
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
        ,'Referer':'https://pearvideo.com/video_%s'%true_videotitle
    }
    requests_url1='https://pearvideo.com/videoStatus.jsp?contId=%s&mrd=0.08126435144831268'%true_videotitle
    json_data=requests.get(url=requests_url1,headers=headers1).json()
    hrefdata=json_data['videoInfo']['videos']['srcUrl']
    href_list=hrefdata.split('/')
    
    href_list2=href_list[6].split('-')[1] #用来存放具有第二种特征数字的字符串
    
    
    new_href_list=[]
    #将列表重新拼接成字符串来实现完整地址的目的
    for i in range(0,6):
        new_href_list.append(href_list[i]+'/')
    new_href_list.append('cont-'+true_videotitle+'-'+href_list2+'-ad_hd.mp4')
    
    video_src=''
    for i in new_href_list:
        video_src=video_src+i
    #将视频名字和链接存放到字典中，再把字典存到列表中
    dic={
        'name':true_videotitle,
        'url':video_src
    }
    urls.append(dic)
#获取响应数据和持久化存储的函数
def getvideo_data(dic):
    url=dic['url']
    data = requests.get(url=url,headers=headers).content#持久化存储操作
    video_path = 'picLibs/' + dic['name'] + '.mp4'
    with open(video_path,'wb')as fp:
        fp.write(data)
        print(dic['name'],'下载成功!')

#使用线程池对视频数据进行请求
if __name__=='__main__':
    pool=Pool(5)
    pool.map(getvideo_data,urls)
    pool.close()
    pool.join()
