# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban250.items import Douban250Item

class Movie250Spider(CrawlSpider):
    name = 'movie250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']
    #提取下一页链接
    page_links = LinkExtractor(allow = r'start=\d+')
    
    #提取页面中的电影链接
    movie_links = LinkExtractor(allow = r'/subject/\d+')

    #确定爬取的页面
    rules = (
        Rule(page_links, follow = True),
        Rule(movie_links, callback='parse_item')
    )
    

    def parse_item(self, response):
        item = Douban250Item()
        item['url'] = response.url
        item['title'] = response.xpath('//h1/span[1]/text()').extract()[0]
        #提取类型，因为含有多个类型，所以将数据保存为一个列表
        item['type_'] = response.xpath('//span[@property="v:genre"]/text()').extract()
        item['star'] = response.xpath('//strong[@property="v:average"]/text()').extract()[0]
        #因为简介中含有br标签，无法完成一次性提取，故以迭代的方式提取内容
        summary = ''
        for str in response.xpath('//span[@property="v:summary"]/text()').extract():
            summary += str
        item['summary'] = summary.replace(' ','').strip()
        yield item
