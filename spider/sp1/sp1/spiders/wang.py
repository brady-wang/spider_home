# -*- coding: utf-8 -*-
from time import sleep

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WangSpider(CrawlSpider):
    name = 'wang'
    allowed_domains = ['www.7160.com']
    start_urls = ['http://www.7160.com']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.7160.com.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}

        title_list = response.xpath('/html/body/div/div[2]/div[1]/div[2]/h1/text()').extract()
        img_url_list = response.xpath('/html/body/div/div[2]/div[1]/div[2]/div[3]/p/a/img/@src').extract()
        print("***************************************************************")
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        if(len(title_list) > 0 and len(img_url_list) > 0 ):
            i['title'] = title_list[0]
            i['img_url'] = img_url_list[0]
            yield i
        else:
            print("不是需要的页面"+response.url)