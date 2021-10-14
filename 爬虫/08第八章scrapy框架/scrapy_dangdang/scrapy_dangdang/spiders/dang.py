import scrapy
from scrapy_dangdang.items import ScrapyDangdangItem


class DangSpider(scrapy.Spider):
    name = 'dang'
    
    #如果是多页下载的话必须调整的是allowed_domains的范围，一般情况下只写域名
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']
    page=1
    base_url = 'http://category.dangdang.com/pg'
    def parse(self, response):
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            if src:
                src=src
            else:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            book = ScrapyDangdangItem(src=src, name=name, price=price)
            
            #获取一个book就将book交给piplines
            yield book
        
        if self.page < 100:
            self.page =self.page+1
            url=self.base_url+str(self.page)+'-cp01.01.02.00.00.00.html'
            
            #怎么去调用parse方法
            # scrapy.Request 就是scrapy的get请求
            #url就是请求地址
            #callback是你需要执行的那个函数，注意不需要加（）
            yield  scrapy.Request(url=url,callback=self.parse)