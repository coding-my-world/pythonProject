# 崔浩然
# 时间:2021/9/22 16:58
# 功能:验证码识别
import requests
from lxml import etree
from chaojiying import main
#将验证码下载到本地
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }

url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

page_text = requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)

code_img_src='https://so.gushiwen.cn'+tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = requests.get(url=code_img_src,headers=headers).content
with open('./code.jpg','wb') as fp:
    fp.write(img_data)
print(main('code.jpg'))
