# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from tibia.items import TibiaPlayerItem
from tibia.items import TibiaWorldItem
import urlparse
from scrapy.http import Request

class OnlineSpider(scrapy.Spider):
	name = "online"
	allowed_domains = ["tibia.com"]
	start_urls = (
		'http://www.tibia.com/community/?subtopic=worlds&world=',
	)

	def parse(self, response):
		targetUrl = 'http://www.tibia.com/community/?subtopic=worlds&world='
		targetTable = response.xpath("//*[@class=(\"TableContent\")]")[1]
		for tr in targetTable.xpath('.//tr[not(contains(@class,"LabelH"))]'):
			item = TibiaWorldItem()
			link = tr.xpath('td[1]/a')
			url = str(link.xpath('@href').extract())
			item['link'] = url
			name = str(tr.xpath('td[1]/a/text()').extract()).strip().replace('\\xa0', ' ')
			item['name'] = name
			item['location'] = str(tr.xpath('td[3]/text()').extract()).strip().replace('\\xa0', ' ')
			item['pvp']  = str(tr.xpath('td[4]/text()').extract()).strip().replace('\\xa0', ' ')
			item['additionalInformation'] = str(tr.xpath('td[5]/text()').extract()).strip().replace('\\xa0', ' ')
			yield Request(url=url, meta={'item': item}, callback = self.parseWorld)


	def parseWorld(self, response):
		print "test"
		targetTable = response.xpath("//*[@class=(\"InnerTableContainer\")]/table")[3]
		for tr in targetTable.xpath('.//tr[not(contains(@class,"LabelH"))]'):
			item = TibiaPlayerItem()
			item['name'] = str(tr.xpath('td[1]/a/text()').extract()).strip().replace('\\xa0', ' ')
			item['level'] = str(tr.xpath('td[2]/text()').extract()).strip().replace('\\xa0', ' ')
			item['vocation'] = str(tr.xpath('td[3]/text()').extract()).strip().replace('\\xa0', ' ')
			yield item