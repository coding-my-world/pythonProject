# 崔浩然
# 时间:'2021/9/15 18:41',
# 功能：爬取药监总局化妆品公司数据
import requests
import json
if __name__ == '__main__':
    
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    #批量获取不同企业的id值
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3751.400'
    }

    id_list = [] #存储企业ID
    all_data_list = []#存储

    for page in range(1,6):
        page=str(page)
        #参数的封装
        data = {
            'on':'true',
            'page':page,
            'pageSize':'15',
            'productName':'',
            'conditionType':'1',
            'applyname':'',
            'applysn':'',
        }

        json_ids=requests.post(url=url,headers=headers,data=data).json()

        for dic in json_ids['list']:
            dic["ID"]
            id_list.append(dic["ID"])

    #print(id_list)

    #获取企业详情数据
    post_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data={
            'id':id
        }
        detail_json = requests.post(url=post_url,data=data,headers=headers).json()
        all_data_list.append(detail_json)
    fp=open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    fp.close()
    print('over')