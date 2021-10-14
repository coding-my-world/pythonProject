# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#如果想使用管道的话那么就必须在settings中开启管道
class ScrapyDangdangPipeline:
    
    def open_spider(self,spider):
        self.fp = open('book.json', 'w', encoding='utf-8')
        
    def process_item(self, item, spider):
        
        
        self.fp.write(str(item))
        return item
    def close_spider(self,spider):
        self.fp.close()
    
#多条管道类
#1.定义管道类
#2.在settings中开启管道
import urllib.request
class DangDangDownloadPipline:
    def process_item(self,item,spider):
        url = 'http:'+item.get('src')
        filename = './books/'+item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url,filename=filename)
        return item