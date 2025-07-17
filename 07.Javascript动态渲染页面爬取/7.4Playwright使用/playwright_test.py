import playwright
import asyncio
import re
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
"""3.基本使用"""
# 同步
# with sync_playwright() as p:
#     for browser_type in [p.chromium, p.firefox, p.webkit]:
#         browser = browser_type.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://www.baidu.com")
#         page.screenshot(path=f'screenshot-{browser_type.name}.png')
#         print(page.title)
#         browser.close()

# 异步
# async def main():
#     async with async_playwright() as p:
#         for browser_type in [p.chromium, p.firefox, p.webkit]:
#             browser = await browser_type.launch(headless=False)
#             page = await browser.new_page()
#             await page.goto("https://www.baidu.com")
#             await page.screenshot(path=f'screenshot-{browser_type.name}.png')
#             print(await page.title())
#             await browser.close()
#
# asyncio.run(main())

"""4.代码生成"""

"""5.支持移动浏览器"""
# with sync_playwright() as p:
#     iphone_12_pro_max = p.devices['iPhone 12 Pro Max']
#     browser = p.webkit.launch(headless=False)
#     context = browser.new_context(
#         **iphone_12_pro_max,
#         locale='zh-CN'
#     )
#     page = context.new_page()
#     page.goto('https://www.whatismybrowser.com/')
#     page.wait_for_load_state(state='networkidle')
#     page.screenshot(path='browser-iphone.png')
#     browser.close()

"""6.选择器"""
# 文本选择

# CSS选择器

# CSS选择器 + 文本值

# CSS选择器 + 节点关系

# XPath

"""7.常用的操作方法"""
# 事件监听
# def  on_response1(response):
#     print(f'Status {response.status}:{response.url}')
#
# def on_response2(response):
#     if '/api/movie' in response.url and response.status == 200:
#         print(response.json())
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.on('response', on_response2)
#     page.goto('https://spa6.scrape.center/')
#     page.wait_for_load_state('networkidle')
#     browser.close()

# 获取页面源代码
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://spa6.scrape.center/")
#     page.wait_for_load_state('networkidle')
#     html = page.content()
#     print(html)
#     browser.close()

# 页面点击
# page.click(selector, **kwargs)  必须传入参数selector，用来匹配想要点击的节点

# 文本输入
# page.fill(selector, value, **kwargs)
# 必传参数 第一个selector，代表选择器; 第二个value，代表输入的文本内容

# 获取节点属性
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://spa6.scrape.center/")
#     page.wait_for_load_state('networkidle')
#     href = page.get_attribute("a.name", "href")
#     print(href)
#     browser.close()

# 获取多个节点
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://spa6.scrape.center/")
#     page.wait_for_load_state('networkidle')
#     elements = page.query_selector_all("a.name")
#     for element in elements:
#         print(element.get_attribute('href'))
#         print(element.text_content())
#     browser.close()

# 获取单个节点
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://spa6.scrape.center/")
#     page.wait_for_load_state('networkidle')
#     element = page.query_selector("a.name")
#     print(element.get_attribute('href'))
#     print(element.text_content())
#     browser.close()

# 网络劫持 -> 劫持图片

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#
#     def cancel_request(route, request):
#         route.abort()
#     page.route(re.compile(r"(\.png)|(\.jpg)"), cancel_request)
#     page.goto("https://spa6.scrape.center/")
#     page.wait_for_load_state('networkidle')
#     page.screenshot(path='no_picture.png')
#     browser.close()

# 网络劫持 -> 劫持网页
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    def modify_response(route, request):
        route.fulfill(path='./custom_response.html')

    page.route('**/*', modify_response)
    page.goto("https://spa6.scrape.center/")
    page.screenshot(path='custom_page.png')
    browser.close()

"""8.总结"""
