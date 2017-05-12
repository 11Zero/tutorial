# -*- coding: utf-8 -*-

import scrapy
import sys
sys.path.append("..")
from items import DmozItem

class DmozSpider(scrapy.spiders.Spider):
    name = "isudo"
    allowed_domains = ["blog.csdn.net"]
    start_urls = [
        "http://blog.csdn.net/sudoroger"
    ]

    def parse(self,response):
        print "-----------"
        self.log('A response from %s just arrived!' % response.url)
        sel = response.xpath('//div[@id="article_list"]')
        item = DmozItem()
        #result_f = open("1.txt", "w+")
        item['title'] = sel.xpath('//span[@class="link_title"]/a/text()').extract()
        item['link'] = sel.xpath('//span[@class="link_title"]/a/@href').extract()
        item['desc'] = sel.xpath('//div[@class="article_description"]/text()').extract()
        return item
        # print  "-----------"
        # print item['desc']
        # print  "-----------"

            #print tranfor_code(item['title'])

            # str_convert = "%s"%(item['title'])
            # i=3
            # while(i<str_convert.__len__()):
            #     if(str_convert[i] == '\\' and str_convert[i+1] == 'u'):
            #         str_item = str_convert[i:i+6]
            #         i+=6
            #         print ('u'+'\''+'\\'+str_item+'\'').decode('gbk')
            #     else:
            #         str_item=""
            #         while(not (str_convert[i] == '\\' and str_convert[i+1] == 'u')):
            #             str_item+=str_convert[i]
            #             i+=1
            #             if (i == str_convert.__len__()):
            #                 break
            #         print str_item
            # for t in item['title']:
            #     #print t.encode('utf-8')
            #     print t.encode(response.encoding)
            #
            # # #print "TTTTTTTTTT",title,link,desc