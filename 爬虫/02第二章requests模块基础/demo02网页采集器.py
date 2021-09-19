# 崔浩然
# 时间:2021/9/11 20:08
import requests

#门户网站的服务器会检测对应请求的载体的身份标识，如果检测到请求载体身份标识为某一款浏览器
#说明该请求是一个正常的请求。但是检测到请求的载体身份标识不是浏览器的则表示为不正常请求（爬虫）
#服务器端拒绝该次请求
#UA：user-agent(请求载体的身份标识）
if __name__ =='__main__':
    url='https://www.sogou.com/web'
    # UA伪装:将对应的User-Agent封装到一个字典中
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }
    #处理url携带的参数：封装到字典中
    kw=input('enter a word:')
    param = {
        'query':kw
    }
    response=requests.get(url=url,params=param,headers=headers)
    page_text=response.text
    filename=kw+'.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename,'保存成功！！！')