import scrapy
from scrapy_splash import SplashRequest
import re

from scrapysplashdemo.items import BookItem

script = """
function main(splash, args)
    assert(splash:go(args.url))
    assert(splash:wait(5))
    return splash:html()
end
"""


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["spa5.scrape.center"]
    start_urls = "https://spa5.scrape.center"

    def start_requests(self):
        start_url = f'{self.start_urls}/page/1'
        yield SplashRequest(url=start_url,  endpoint='execute', args={'lua_source': script}, callback=self.parse_index)

    def parse_index(self, response):
        items = response.css('.item')
        for item in items:
            href = item.css('.top a::attr(href)').extract_first()
            detail_url = response.urljoin(href)
            print(detail_url)
            yield SplashRequest(url=detail_url, callback=self.parse_detail, priority=2,
                                args={'lua_source': script}, endpoint='execute')

        # match = re.search('page/(\d+)', response.url)
        # if not match: return
        # page = int (match.group(1)) + 1
        # next_url = f'{self.start_urls}/page/{page}'
        # yield SplashRequest(url=next_url, callback=self.parse_index, args={'lua_source': script}, endpoint='execute')

    def parse_detail(self, response):
        # print("信息开始================================================================")
        name = response.css('.name::text').extract_first()
        tags = response.css('.tags button span::text').extract()
        score = response.css('.score::text').extract_first()
        price = response.css('.price span::text').extract_first()
        cover = response.css('.cover::attr(src)').extract_first()
        tags = [tag.strip() for tag in tags] if tags else []
        score = score.strip() if score else None
        # print(f'name:{name}')
        # print(f'tags:{tags}')
        # print(f'score:{score}')
        # print(f'price:{price}')
        # print(f'cover:{cover}')
        # print("信息结束================================================================")
        item = BookItem(name=name, tags=tags, score=score, price=price, cover=cover)
        yield item
