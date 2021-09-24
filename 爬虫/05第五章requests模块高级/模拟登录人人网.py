# 崔浩然
# 时间:2021/9/23 9:13
# 功能：模拟人人网登录
# 编码流程：
#     1.验证码的识别，获取验证码图片的文字数据
#     2.对get请求进行发送
#     3.对响应数据进行持久化存储

import requests
from chaojiying import img_data_number
from lxml import etree
#创建会话对象，该会话对象可以调用get和post发起请求
session = requests.Session()

# 1.对验证码图片进行捕获和识别
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3872.400 QQBrowser/10.8.4455.400',
    'Referer': 'http://www.renren.com/SysHome.do'
}
#创建会话对象,该会话对象可以调用get和post发起请求
session = requests.Session()

# 1.对验证码图片进行捕获和识别
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Referer': 'http://www.renren.com/SysHome.do',
        }
url = 'http://www.renren.com/'
page_text = session.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
img_url = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
print(img_url)
img_data = session.get(img_url,headers=headers).content
print(img_data)
with open('./code.jpg','wb') as fp:
    fp.write(img_data)

# 使用超级鹰打码提供的示例代码对验证码图片进行识别
result=img_data_number('code.jpg')


login_post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=202112910495'
data = {
    'email': '910451393@qq.com',
    'icode': result,
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '346d050fe82d3cfe090210864d73b65b5608bf90173371b3c10e7df6e533',
    'rkey': '3a7cdde0b042c1ba11169c3378fd5b',
    'f': 'http%3A%2F%2Fwww.renren.com%2F974713149%2Fnewsfeed%2Fphoto'
}
response = session.post(url=login_post_url, headers=headers,data=data)
print(response.text)


# 2.对get请求进行发送

login_url = 'http://www.renren.com/974713149'
login_page_text = session.get(url=login_url, headers=headers).text
with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(login_page_text)


# 爬取当前用户的个人主页对应的页面数据
detail_url = 'http://www.renren.com/974713149/profile'
detail_page_text = session.get(url=detail_url, headers=headers).text
with open('zep.html','w',encoding='utf-8') as fp:
    fp.write(detail_page_text)
