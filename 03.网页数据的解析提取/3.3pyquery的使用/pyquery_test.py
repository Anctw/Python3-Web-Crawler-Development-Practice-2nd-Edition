from pyquery import PyQuery as pq

"""2.初始化"""
# 字符串初始化
# html = """
# <div>
#     <ul>
#         <li class="item-0">first item</li>
#         <li class="item-1"><a href="link2.html">second item</a></li>
#         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#         <li class="item-0"><a href="link5.html">fifth item</a></li>
#     </ul>
# </div>
# """
#
# doc = pq(html)
# print(doc('li'))
# URL初始化
# doc = pq(url='https://cuiqingcai.com')
# print(doc('title'))

# 文件初始化
# doc = pq(filename='demo.html')
# print(doc('li'))

"""3.基本的CSS选择器"""
# html = """
# <div id="container">
#     <ul class="list">
#         <li class="item-0">first item</li>
#         <li class="item-1"><a href="link2.html">second item</a></li>
#         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#         <li class="item-0"><a href="link5.html">fifth item</a></li>
#     </ul>
# </div>
# """
# doc = pq(html)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))
# for item in doc('#container .list li').items():
#     print(item.text())

"""4.查找节点"""
# 子节点
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')
# print(type(lis))
# print(lis)
# liss = items.children()
# print(type(liss))
# print(liss)

# 父节点
# html = """
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#             <li class="item-0"><a href="link0.html">first item</a></li>
#             <li class="item-1"><a href="link2.html">second item</a></li>
#             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#             <li class="item-0"><a href="link5.html">fifth item</a></li>
#         </ul>
#     </div>
# </div>
# """
# doc = pq(html)
# items = doc('.list')
# container = items.parent()
# print(type(container))
# print(container)
# print("=========================")
# parents = items.parents()
# print(type(parents))
# print(parents)
# print("=========================")
# parent = items.parents('.wrap')
# print(parent)
# 兄弟节点
# doc = pq(html)
# li = doc('.list .item-0.active')
# print(li.siblings())
# print("=============================")
# print(li.siblings(".active"))
"""5.遍历节点"""
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# print(str(li))
# print("============================")
# lis = doc('li').items()
# print(type(lis))
# for li in lis:
#     print(li, type(li))

# 获取属性
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a, type(a))
# print(a.attr('href'))
# print("==========================")
# ass = doc('a')
# for item in ass.items():
#     print(item.attr.href)

# 获取文本
# print("==========================")
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a.text())
# print("==========================")
# li = doc('.item-0.active')
# print(li)
# print(li.html())
# print("==========================")
# lis = doc('li')
# print(lis.html())
# print(lis.text())
# print(type(lis.text()))

"""6.节点操作"""
# addClass 和 removeClass
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.remove_class('active')
# print(li)
# li.add_class('active')
# print(li)

# attr\text和html
# html = """
# <ul class="list">
#             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# </ul>
# """
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.attr('name', 'link')
# print(li)
# li.text('changed item')
# print(li)
# li.html('<span>changed item</span>')
# print(li)

# remove
# html = """
# <div class="wrap">
#     Hello, World
#     <p>This is a paragraph.</p>
# </div>
# """
# doc = pq(html)
# wrap = doc('.wrap')
# print(wrap.text())
# print("=================================")
# wrap.find('p').remove()
# print(wrap.text())

"""7.伪类选择器"""
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
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)











