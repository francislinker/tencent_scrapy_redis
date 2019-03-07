# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .settings import *

class TencentPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(MYSQL_HOST,MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.col = self.db[MONGO_SET]
    def process_item(self, item, spider):
        print("*"*50)
        print(item['zhName'])
        print(item['zhType'])
        print(item['zhNum'])
        print(item['zhAddress'])
        print(item['zhtime'])
        print(item['zhlink'])
        print("*"*50)

        recruitinfo = {
                'zhName':item['zhName'],
                'zhType':item['zhType'],
                'zhNum':item['zhNum'],
                'zhAddress':item['zhAddress'],
                'zhtime':item['zhtime'],
                'zhlink':item['zhlink']
        }
        self.col.insert_one(recruitinfo)


        return item
