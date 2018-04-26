# -*- coding: utf-8 -*-
import scrapy


class YongSpider(scrapy.Spider):
    name = 'yong'
    allowed_domains = ['www.7160.com']
    start_urls = ['http://www.7160.com/']

    def parse(self, response):
        pass
