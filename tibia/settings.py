# -*- coding: utf-8 -*-

# Scrapy settings for tibia project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tibia'

SPIDER_MODULES = ['tibia.spiders']
NEWSPIDER_MODULE = 'tibia.spiders'
ITEM_PIPELINES = {
	'tibia.pipelines.TibiaPipeline' : 300
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'tstats (+http://www.yourdomain.com) mk@trou.pl'
