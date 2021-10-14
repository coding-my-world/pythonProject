import scrapy
from scrapy_movie.items import ScrapyMovieItem

class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/china/index.html']

    def parse(self, response):
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')
        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            
            #第二页地址
            url = 'https://www.dytt8.net' + href
            
            #对第二页的链接发起访问
            yield scrapy.Request(url=url, callback=self.parse_second,meta={'name':name})
            
    def parse_second(self,response):
        #如果拿不到数据的情况下，一定检查你的xpath语法是否正确
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        
        # 接受到请求的那个meta参数的值
        name = response.meta['name']
        
        movies = ScrapyMovieItem(src=src, name=name)
        
        yield movies