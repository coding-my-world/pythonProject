# 崔浩然
# 时间:2021/9/24 15:11
# 功能：个人主页获取
# 崔浩然
# 时间:2021/9/23 9:13
# 功能：模拟人人网登录
# 编码流程：
#     1.验证码的识别，获取验证码图片的文字数据
#     2.对get请求进行发送
#     3.对响应数据进行持久化存储
import requests
import json
# 创建会话对象，该会话对象可以调用get和post发起请求
session = requests.Session()
# 1.对验证码图片进行捕获和识别
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3872.400 QQBrowser/10.8.4455.400',
    
}
# 创建会话对象,该会话对象可以调用get和post发起请求
session = requests.Session()

# 1.对验证码图片进行捕获和识别
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
}
login_url = 'https://rrwapi.renren.com/account/v1/loginByPassword'
data = {
    "user": "13934250220",
    "password": "fef26a8b8c43690fc4c3d43f6b305a1d",
    "appKey": "bcceb522717c2c49f895b561fa913d10",
    "sessionKey": "",
    "callId": "1632471324948",
    "sig": "3b0ac55e70675221af813bdfa11b09fa"
}
response= session.post(url=login_url,data=data,headers=headers)

