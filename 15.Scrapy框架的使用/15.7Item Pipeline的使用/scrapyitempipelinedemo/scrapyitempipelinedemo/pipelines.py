# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from typing import Any

import scrapy.pipelines.images
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from elasticsearch import Elasticsearch
from scrapy.http import Response
from scrapy.pipelines.media import FileInfoOrError, MediaPipeline

from scrapyitempipelinedemo.item import MovieItem
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class ScrapyitempipelinedemoPipeline:
    def process_item(self, item, spider):
        return item


class MongoDBPipline(object):

    @classmethod
    def from_crawler(cls, crawler):
        cls.connection_string = crawler.settings.get('MONGODB_CONNECTION_STRING')
        cls.database = crawler.settings.get('MONGODB_DATABASE')
        cls.collection = crawler.settings.get('MONGODB_COLLECTION')
        return cls()


    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.connection_string)
        self.db = self.client[self.database]

    def process_item(self, item, spider):
        self.db[self.collection].update_one({
            'name': item['name']
        }, {
            '$set': dict(item)
        }, True)
        return item


    def close_spider(self, spider):
        self.client.close()


class ElasticsearchPipline(object):
    @classmethod
    def from_crawler(cls, crawler):
        cls.connection_string = crawler.settings.get('ELASTICSEARCH_CONNECTION_STRING')
        cls.index = crawler.settings.get('ELASTICSEARCH_INDEX')
        return cls()

    def open_spider(self, spider):
        self.conn = Elasticsearch(hosts=[f'{self.connection_string}'])
        conn1 = (self.conn.indices.exists(index=self.index))
        if not conn1:
            self.conn.indices.create(index=self.index)

    def process_item(self, item, spider):
        self.conn.index(index=self.index, body=dict(item), id=hash(item['name']))
        return item

    def close_spider(self, spider):
        self.conn.transport.close()


class ImagePipeline(ImagesPipeline):

    # def file_path(self, request, response=None, info=None):
    def file_path(
        self,
        request: Request,
        response: Response | None = None,
        info: MediaPipeline.SpiderInfo | None = None,
        *,
        item: Any = None,
    ) -> str:
        movie = request.meta['movie']
        type = request.meta['type']
        name = request.meta['name']
        file_name = f'{movie}/{type}/{name}.jpg'
        return file_name

    # def item_completed(self, results, item, info):
    def item_completed(
        self, results: list[FileInfoOrError], item: Any, info: MediaPipeline.SpiderInfo
    ) -> Any:

        images_paths = [x['path'] for ok, x in results if ok]
        if not images_paths:
            raise DropItem('Image Downloaded Failed')
        return item

    # def get_media_requests(self, item, info):
    def get_media_requests(
        self, item: Any, info: MediaPipeline.SpiderInfo
    ) -> list[Request]:
        for director in item['directors']:
            director_name = director['name']
            director_image = director['image']
            yield Request(director_image, meta={
                'name': director_name,
                'type': 'director',
                'movie': item['name']
            })

        for actor in item['actors']:
            actor_name = actor['name']
            actor_image = actor['image']
            yield Request(actor_image, meta={
                'name': actor_name,
                'type': 'actor',
                'movie': item['name']
            })














