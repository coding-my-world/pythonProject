import scrapy


class FirstSpider(scrapy.Spider):
    #name:爬虫文件的名称
    name = 'first'
    #允许的域名：不在此允许范围内的域名就会被过滤，而不会进行爬取
    # 对于start_urls里的起始爬取页面，它是不会过滤的，它的作用是过滤首页之后的页面
    allowed_domains = ['www.xxx.com']
    #起始的url列表：该列表中存放的url会被scrapy自动进行请求的发送
    start_urls = ['https://www.baidu.com/','https://www.sougou.com']

    #用作于数据解析
    def parse(self, response):
        print(response)
