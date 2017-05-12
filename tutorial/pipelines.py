# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class TutorialPipeline(object):
#     def process_item(self, item, spider):
#         return item
import codecs

class TutorialPipeline(object):

    def __init__(self):
        self.file = codecs.open('items.txt', 'w', encoding='utf-8')
        #self.file = open('items.json', 'wb')

    def process_item(self, item, spider):
        item_link = item['link']
        item_title = item['title']
        item_desc = item['desc']
        nCount = len(item_link)
        for i in range(nCount):
            str = "%s\t%s\t%s" % (item_link[i].replace("\r\n", "").replace("\t", "").replace(" ", ""),
                                item_title[i].replace("\r\n", "").replace("\t", "").replace(" ", ""),
                                item_desc[i][:50].replace("\r\n", "").replace("\t", "").replace(" ", ""))
            #str.replace("\r\n", "")
            self.file.write(str+"\r\n")
        # for it_link,it_title,it_desc in item_link,item_title,item_desc:
        #     str = "1232"  #"%s,%s,%s" % ("".join(it_link),"".join(it_title),"".join(it_desc))
        #     self.file.write(str)
        #line = "".join(item_title)+"\r\n"
        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #self.file.write(line)
        return item