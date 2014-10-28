# -*- coding: utf-8 -*-
import scrapy
from tibia.items import TibiaPlayerItem
from tibia.items import TibiaWorldItem
from scrapy.http import Request

class OnlineSpider(scrapy.Spider):
    name = "online"
    allowed_domains = ["tibia.com"]
    start_urls = (
        'http://www.tibia.com/community/?subtopic=worlds&world=',
    )

    def parse(self, response):
        targetTable = response.xpath("//*[@class=(\"TableContent\")]")[1]
        for tr in targetTable.xpath('.//tr[not(contains(@class,"LabelH"))]'):
            item = TibiaWorldItem()
            link = tr.xpath('td[1]/a')
            url = link.xpath('@href').extract()
            item['link'] = url[0]
            name = tr.xpath('td[1]/a/text()').extract()[0].strip().replace('\\xa0', ' ')
            item['name'] = name
            item['location'] = tr.xpath('td[3]/text()').extract()[0].strip().replace('\\xa0', ' ')
            item['pvp'] = tr.xpath('td[4]/text()').extract()[0].strip().replace('\\xa0', ' ')
            item['additionalInformation'] = str(tr.xpath('td[5]/text()').extract()).strip().replace('\\xa0', ' ')
            item['players'] = []
            yield Request(url=url[0], callback = self.parseWorld, meta={'item': item})
            

    def parseWorld(self, response):
        targetTable = response.xpath("//*[@class=(\"InnerTableContainer\")]/table")[2]
        world = response.meta['item']
        for tr in targetTable.xpath('.//tr[not(contains(@class,"LabelH"))]'):
            item = TibiaPlayerItem()
            item['name'] = tr.xpath('td[1]/a[last()]/text()').extract()[0].strip().replace('\\xa0', ' ')
            item['level'] = tr.xpath('td[2]/text()').extract()[0].strip().replace('\\xa0', ' ')
            item['vocation'] = tr.xpath('td[3]/text()').extract()[0].strip().replace('\\xa0', ' ')
            world['players'].append(item)
        return world