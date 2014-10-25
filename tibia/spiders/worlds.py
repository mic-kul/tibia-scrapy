# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from tibia.items import TibiaWorldItem

class WorldsSpider(scrapy.Spider):
	name = "worlds"
	allowed_domains = ["tibia.com"]
	start_urls = (
		'http://www.tibia.com/community/?subtopic=worlds',
	)

	def parse(self, response):

		targetTable = response.xpath("//*[@class=(\"TableContent\")]")[1]
		for tr in targetTable.xpath('.//tr[not(contains(@class,"LabelH"))]'):
			item = TibiaWorldItem()
			item['name'] = str(tr.xpath('td[1]/a/text()').extract()).strip().encode('utf8').replace('\\xa0', ' ')
			item['location'] = str(tr.xpath('td[3]/text()').extract()).strip().encode('utf8').replace('\\xa0', ' ')
			item['pvp']  = str(tr.xpath('td[4]/text()').extract()).strip().encode('utf8').replace('\\xa0', ' ')
			item['additionalInformation'] = str(tr.xpath('td[5]/text()').extract()).strip().encode('utf8').replace('\\xa0', ' ')
			
			yield item