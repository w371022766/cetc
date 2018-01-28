# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CetcPipeline(object):
    def process_item(self, item, spider):
        with open("news.txt", 'a') as fp:
            fp.write(item['title'].encode("utf8") + '\t' + item['url'].encode("utf8") + '\t' + item['date'].encode("utf8") + '\n')
