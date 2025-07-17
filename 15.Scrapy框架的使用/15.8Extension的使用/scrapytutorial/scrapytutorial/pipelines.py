# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
import pymongo


class TextPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].rstrip() + '...'
            return item
        else:
            return DropItem('Missing Text')


# class MongoPipeline:
#     def __int__(self):
#         settings = get_project_settings()
#         self.connection_string = settings['MONGODB_CONNECTION_STRING']
#         self.database = settings['MONGODB_DATABASE']
#
#     # @classmethod
#     # def from_crawler(cls, crawler):
#     #     cls.connection_string = crawler.settings.get('MONGODB_CONNECTION_STRING',  'mongodb://localhost:27017/')
#     #     cls.database = crawler.settings.get('MONGODB_DATABASE', 'scrapytutorial')
#     #     return cls
#
#     def open_spider(self):
#         self.client = pymongo.MongoClient(self.connection_string)
#         self.db = self.client[self.database]
#
#     def process_item(self, item, spider):
#         name = item.__class__.__name__
#         self.db[name].insert_one(dict(item))
#         return item
#
#     def close_spider(self, spider):
#         self.client.close()

class MongoDBPipeline(object):

    def __init__(self, connection_string, database):
        self.connection_string = connection_string
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            connection_string=crawler.settings.get('MONGODB_CONNECTION_STRING'),
            database=crawler.settings.get('MONGODB_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.connection_string)
        self.db = self.client[self.database]

    def process_item(self, item, spider):
        name = item.__class__.__name__
        self.db[name].insert_one(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
