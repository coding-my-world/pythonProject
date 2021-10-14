import logging

import scrapy
import logging

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        for i in range(10):
            item={}
            item['come_from'] = "itcast"
            logging.warning(item)
