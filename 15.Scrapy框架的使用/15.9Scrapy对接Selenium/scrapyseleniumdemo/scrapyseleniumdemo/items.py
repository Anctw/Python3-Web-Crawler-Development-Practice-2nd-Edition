# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    name = Field()
    tags = Field()
    score = Field()
    cover = Field()
    price = Field()
    # pass
