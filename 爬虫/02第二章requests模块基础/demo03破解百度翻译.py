# 崔浩然
# 时间:2021/9/12 18:44
import json

import requests
if __name__=='__main__':
    #指定url
    post_url='https://fanyi.baidu.com/sug'
    
    #post请求参数处理（同get请求一致）
    input=input('输入需要翻译的内容：')
    data={
        'kw':input
    }
    
    #进行UA伪装
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.44'
    }
    
    #请求发送
    response=requests.post(url=post_url,data=data,headers=headers)
    
    #获取响应数据；json方法返回obj（如果确认响应数据是json类型的才可以使用json（））
    dic_obj = response.json()
    
    #持久化存储
    fp = open('./dog.json','w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    fp.close()
    print('over!!!')
    