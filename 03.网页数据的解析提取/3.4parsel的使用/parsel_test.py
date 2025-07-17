"""说明 124，125页，电子书中缺失"""
from parsel import Selector
html = """
<div class="wrap">
    <div id="container">
        <ul class="list">
            <li class="item-0"><a href="link0.html">first item</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
</div>
"""

"""4.使用Xpath语法"""
# selector = Selector(text=html)
# result1 = selector.xpath('//li[contains(@class, "item-0")]//text()').get()
# print(type(result1))
# print(result1)
# result2 = selector.xpath('//li[contains(@class, "item-0")]//text()').getall()
# print(result2)
# result3 = selector.css('.item-0 *::text').getall()
# print(result3)

"""5.提取属性"""
# selector = Selector(text=html)
# result1 = selector.css('.item-0.active a::attr(href)').get()
# print(result1)
# result2 = selector.xpath('//li[contains(@class, "item-0") and contains(@class, "active")]/a/@href').get()
# print(result2)


"""6.正则提取"""
selector = Selector(text=html)
result1 = selector.css('.item-0').re('link.*')
print(result1)

result2 = selector.css('.item-0 *::text').re('.*item')
print(result2)

result3 = selector.css('.item-0').re_first('<span class="bold">(.*?)</span>')
print(result3)



