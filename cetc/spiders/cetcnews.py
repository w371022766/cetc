# -*- coding: utf-8 -*-
import scrapy
from cetc.items import CetcItem

class CetcnewsSpider(scrapy.Spider):
    name = 'cetcnews'
    allowed_domains = ['cetc.com.cn']
    start_urls = []
    for i in range(1, 11):
        start_urls.append('http://www.cetc.com.cn/zgdzkj/_300931/_300935/9765e8fb-' + str(i) + '.html')
    def parse(self, response):
        articles = response.xpath('//*[@id="ContentPane"]/ul/li')
        for article in articles:
            item = CetcItem()
            item['title'] = article.xpath('./span[1]/a/@title').extract()[0]
            item['url'] = article.xpath('./span[1]/a/@href').extract()[0]
            item['date'] = article.xpath('./span[2]/text()').extract()[0]
            yield item
