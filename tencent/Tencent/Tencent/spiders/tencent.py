
# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentItem
from scrapy_redis.spiders import RedisSpider
class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?start=0']
    baseurl = 'https://hr.tencent.com/position.php?start='
    def parse(self, response):
        #把要爬取的url地址交给调度器
        for page in range(0,1000,10):
            url = self.baseurl+str(page)
            print(url)
            #交给调度器,并指定解析函数
            yield scrapy.Request(url,callback=self.getHtml)

    def getHtml(self,response):

        #创建item对象
        item = TencentItem()
        #基准xpath节点对象列表
        baseList = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        for base in baseList:
            item['zhName'] = base.xpath('./td[1]/a/text()').extract()[0]
            item['zhType'] = base.xpath('./td[2]/text()')
            if item['zhType']:
                item['zhType'] = base.xpath('./td[2]/text()').extract()[0]
            else:
                item['zhType'] = '无'
            item['zhNum'] = base.xpath('./td[3]/text()').extract()[0]
            item['zhAddress'] = base.xpath('./td[4]/text()').extract()[0]
            item['zhtime'] = base.xpath('./td[5]/text()').extract()[0]
            item['zhlink'] = 'https://hr.tencent.com/'+base.xpath('./td[1]/a/@href').extract()[0]
            print(item['zhlink'])

            yield item



