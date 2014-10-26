# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TibiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TibiaWorldItem(scrapy.Item):
	link = scrapy.Field()
	name = scrapy.Field()
	pvp = scrapy.Field()
	location = scrapy.Field()
	additionalInformation = scrapy.Field()
	players = scrapy.Field()

class TibiaPlayerItem(scrapy.Item):
	name = scrapy.Field()
	level = scrapy.Field()
	vocation = scrapy.Field()