# 崔浩然
# 时间:2021/9/27 14:51
# 功能：简单使用selenium
from selenium import webdriver
from lxml import etree
from time import sleep
#实例化一个浏览器对象（传入浏览器的驱动程序）
bro=webdriver.Chrome(executable_path='./chromedriver.exe')
url='http://scxk.nmpa.gov.cn:81/xk/'

bro.get(url)
page_text = bro.page_source

#解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name=li.xpath('./dl/@title')[0]
    print(name)
sleep(5)
bro.quit()