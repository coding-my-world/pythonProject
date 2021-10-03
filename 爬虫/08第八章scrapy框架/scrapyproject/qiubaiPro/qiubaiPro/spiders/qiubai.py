import scrapy
from qiubaiPro.items import QiubaiproItem

# class QiubaiSpider(scrapy.Spider):
#     name = 'qiubai'
#     # allowed_domains = ['www.qiubai.com']
#     start_urls = ['https://www.qiushibaike.com/text/']
#
#     def parse(self, response):
#         # 解析：作者的名称+段子内容
#         div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
#
#         #存放所有解析到的数据
#         all_data=[]
#         for div in div_list:
#             # xpath返回的是列表，但是列表元素一定是Selector类型的对象
#             # extract可以将Selector对象中data参数存储的字符串提取出来
#             author = div.xpath('.//h2/text()')[0].extract()
#             # 列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取出来
#             content = div.xpath('./a/div/span//text()').extract()
#             content = ''.join(content)
#
#             dic = {
#                 'author':author,
#                 'content':content
#             }
#             all_data.append(dic)
#         return all_data
class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.qiubai.com']
    start_urls = ['https://www.qiushibaike.com/text/']
    
    def parse(self, response):
        # 解析：作者的名称+段子内容
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')

        # 存放所有解析到的数据
        all_data = []
        for div in div_list:
            # xpath返回的是列表，但是列表元素一定是Selector类型的对象
            # extract可以将Selector对象中data参数存储的字符串提取出来
            author = div.xpath('.//h2/text()')[0].extract()
            # 列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取出来
            content = div.xpath('./a/div/span//text()').extract()
            content = ''.join(content)
            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content
            
            yield item # 将item提交给了管道