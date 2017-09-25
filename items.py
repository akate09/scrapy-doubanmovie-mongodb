# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Douban250Item(scrapy.Item):
    # define the fields for your item here like:
    #影片链接
    url = scrapy.Field()
    #影片标题
    title = scrapy.Field()
    #影片类型，为列表
    type_ = scrapy.Field()
    #影片评分
    star = scrapy.Field()
    #影片简介
    summary = scrapy.Field()

