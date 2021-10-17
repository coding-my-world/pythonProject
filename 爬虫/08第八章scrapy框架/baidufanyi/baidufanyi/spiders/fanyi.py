import scrapy
import json

class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    allowed_domains = ['fanyi.baidu.com']
    #start_urls = ['https://fanyi.baidu.com']
    #post请求 如果没有参数 那么这个请求将没有意义
    #所有start_urls 也没有用了
    #parse方法也没有用了
    
    # def parse(self, response):
    #     pass
    def start_requests(self):
        url = 'https://fanyi.baidu.com/langdetect'
        
        data = {
            'query':'final'
        }
        
        yield scrapy.FormRequest(url=url,formdata=data, callback=self.parse_second)
    
    def parse_second(self,response):
        content = response.text
        
        obj = json.loads(content)
        print(obj)