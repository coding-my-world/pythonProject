import scrapy


class Quanzhan1Spider(scrapy.Spider):
    name = 'quanzhan1'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['https://book.qidian.com/info/1028099342/#Catalog']
    
    #生成一个通用的url模板（不可变）
    url = 'https://book.qidian.com/info/1028099342/#Catalog%d'
    page_num=2
    def parse(self, response):
        li_list=response.xpath('//*[@id="j-catalogWrap"]/div[2]/div[1]/ul/li')
        for li in li_list:
            novel_name=li.xpath('./a/text()').extract_first()
            print(novel_name)
        
        if self.page_num<=11:
            new_url = format(self.url%self.page_num)
            self.page_num+=1
            #手动请求发送callback回调函数是专门用于数据解析
            yield scrapy.Request(url=new_url,callback=self.parse)