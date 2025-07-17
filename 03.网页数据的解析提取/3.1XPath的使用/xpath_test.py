from lxml import etree

"""4.实例引入"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))

"""5.所有节点"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//*')
# result = html.xpath('//li')
# print(result)


"""6.子节点"""
# / 获取直接子节点 // 获取子孙节点
# html = etree.parse('./test.html', etree.HTMLParser())
# # result = html.xpath('//li/a')
# result = html.xpath('//ul//a')
# print(result)

"""7.父节点"""
# html = etree.parse('./test.html', etree.HTMLParser())
# # result = html.xpath('//a[@href="link4.html"]/../@class')
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result)


"""8.属性匹配"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]')
# print(result)


"""9.文本获取"""
# html = etree.parse('./test.html', etree.HTMLParser())
# # result = html.xpath('//li[@class="item-0"]/text()')
# # result = html.xpath('//li[@class="item-0"]/a/text()')
# result = html.xpath('//li[@class="item-0"]//text()')
# print(result)


"""10.属性获取"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result)

"""11.属性多值匹配"""
# text = '''
# <li class="li li-first"><a href="link1.html">first item</a></li>
# '''
# html = etree.HTML(text)
# # result = html.xpath('//li[@class="li"]/a/text()')
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)

"""12.多属性匹配"""
# text = '''
# <li class="li li-first" name="item"><a href="link1.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# print(result)

"""13.按序选择"""
# text = '''
# <div>
#     <ul>
#         <li class="item-0"><a href="link1.html">first item</a></li>
#         <li class="item-1"><a href="link2.html">second item</a></li>
#         <li class="item-inactive"><a href="link3.html">third item</a></li>
#         <li class="item-1"><a href="link4.html">fourth item</a></li>
#         <li class="item-0"><a href="link5.html">fifth item</a>
#     </ul>
# </div>
# '''
# html = etree.HTML(text)
# result1 = html.xpath('//li[1]/a/text()')
# print(result1)
# result2 = html.xpath('//li[last()]/a/text()')
# print(result2)
# result3 = html.xpath('//li[position()<3]/a/text()')
# print(result3)
# result4 = html.xpath('//li[last()-2]/a/text()')
# print(result4)


"""14.节点轴选择"""
text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''
html = etree.HTML(text)
result1 = html.xpath('//li[1]/ancestor::*')
print(result1)
result2 = html.xpath('//li[1]/ancestor::div')
print(result2)
result3 = html.xpath('//li[1]/attribute::*')
print(result3)
result4 = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result4)
result5 = html.xpath('//li[1]/descendant::span')
print(result5)
result6 = html.xpath('//li[1]/following::*[3]')
print(result6)
result7 = html.xpath('//li[1]/following-sibling::*')
print(result7)
