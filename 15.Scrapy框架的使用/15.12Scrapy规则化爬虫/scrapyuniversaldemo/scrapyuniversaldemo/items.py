# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, Identity, Compose


class ScrapyuniversaldemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MovieItem(Item):
    name = Field()
    cover = Field()
    categories = Field()
    published_at = Field()
    drama = Field()
    score = Field()


class MovieItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    categories_out = Identity()
    score_out = Compose(TakeFirst(), str.strip)
    drama_out = Compose(TakeFirst(), str.strip)
