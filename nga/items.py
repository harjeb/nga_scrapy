# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NgaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    postnum = scrapy.Field()
    posttime = scrapy.Field()
    posttitle = scrapy.Field()
    postarea = scrapy.Field()
    pass
