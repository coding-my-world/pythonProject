# 崔浩然
# 时间:2021/9/20 18:26
# 功能：xpath解析基础
from lxml import etree

if __name__ == '__main__':
    #实例化好了一个etree对象，且将被解析的源码加载到了该对象中
    tree = etree.parse('text.html')
    print(tree.xpath('/html/body/div'))
    print(tree.xpath('/html//div'))
    print(tree.xpath('//div'))
    print(tree.xpath('//div[@class="song"]'))
    print(tree.xpath('//div[@class="song"]/p[3]'))
    print(tree.xpath('//div[@class="tang"]/ul/li[5]/a/text()')[0])
    print(tree.xpath('//li[7]//text()'))
    print(tree.xpath('//div[class="tang"]//text()'))
    r = tree.xpath('//div[@class="song"]/img/@src')
    
    print(r)
    