import scrapy
from scrapy import Request, Spider
import re
from scrapyseleniumdemo.items import BookItem
from gerapy_selenium import SeleniumRequest


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["spa5.scrape.center"]
    base_urls = "https://spa5.scrape.center"

    def start_requests(self):
        start_url = f'{self.base_urls}/page/1'
        # yield Request(start_url, callback=self.parse_index)
        yield SeleniumRequest(start_url, callback=self.parse_index, wait_for='.item .name')

    def parse_index(self, response):
        items = response.css('.item')
        for item in items:
            href = item.css('.top a::attr(href)').extract_first()
            detail_url = response.urljoin(href)
            print(detail_url)
            yield Request(detail_url, callback=self.parse_detail, priority=2)

        # match = re.search('page/(\d+)', response.url)
        # if not match: return
        # page = int (match.group(1)) + 1
        # next_url = f'{self.base_urls}/page/{page}'
        # yield Request(next_url, callback=self.parse_index)

    def parse_detail(self, response):
        # print("信息开始================================================================")
        name = response.css('.name::text').extract_first()
        tags = response.css('.tags button span::text').extract()
        score = response.css('.score::text').extract_first()
        price = response.css('.price span::text').extract_first()
        cover = response.css('.cover::attr(src)').extract_first()
        tags = [tag.strip() for tag in tags] if tags else[]
        score = score.strip() if score else None
        # print(f'name:{name}')
        # print(f'tags:{tags}')
        # print(f'score:{score}')
        # print(f'price:{price}')
        # print(f'cover:{cover}')
        # print("信息结束================================================================")
        item = BookItem(name=name, tags=tags, score=score, price=price, cover=cover)
        yield item
