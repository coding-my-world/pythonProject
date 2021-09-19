# 崔浩然
# 时间:2021/9/16 8:11
# 功能：爬取糗事百科中糗图板块下所有的糗图图片
import requests
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }
    url='https://pic.qiushibaike.com/system/pictures/12473/124737559/medium/3LEDCVPW4MSOFN3B.jpg'
    
    #content返回的是二进制形式的图片数据
    #text（字符串） content（二进制） json（对象）
    img_data = requests.get(url=url).content
    
    with open('qiutu.jpg', 'wb') as fp:
         fp.write(img_data)