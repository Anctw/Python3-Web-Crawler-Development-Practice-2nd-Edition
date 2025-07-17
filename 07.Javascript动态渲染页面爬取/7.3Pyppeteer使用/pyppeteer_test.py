import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

"""3.快速上手"""
# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('https://spa2.scrape.center/')
#     await page.waitForSelector('.item .name')
#     doc = pq(await page.content())
#     names = [item.text() for item in doc('.item .name').items()]
#     print('Names:', names)
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())

# width, height = 1366, 768
#
# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.setViewport({'width': width, 'height': height})
#     await page.goto('https://spa2.scrape.center/')
#     await page.waitForSelector('.item .name')
#     await asyncio.sleep(2)
#     await page.screenshot(path='example.png')
#     dimensions = await page.evaluate('''() => {
#     return {
#         width: document.documentElement.clientWidth,
#         height:document.documentElement.clientHeight,
#         deviceScaleFactor: window.devicePixelRatio,
#         }
#     }''')
#     print(dimensions)
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())

"""4.launch方法"""

"""5.无头模式"""
# async def main():
#     await launch(headless=False)
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

"""6.调试模式"""
# async def main():
#     browser = await launch(devtools=True)
#     page = await browser.newPage()
#     await page.goto("https://www.baidu.com")
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

"""7.禁用提示条"""
# async def main():
# 新版args=['--disable-infobars']参数不可用
# 使用ignoreDefaultArgs=['--enable-automation']代替，但是有副作用
# browser = await launch(headless=False, args=['--disable-infobars'])
# browser = await launch(headless=False, ignoreDefaultArgs=['--enable-automation'])
# await asyncio.sleep(100)

# asyncio.get_event_loop().run_until_complete(main())

"""8.防止检测"""
# 第一
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto("https://antispider1.scrape.center/")
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

# 第二
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.evaluateOnNewDocument('Object.defineProperties(navigator, {webdriver:{get:()=>undefined}})')
#     await page.goto("https://antispider1.scrape.center/")
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

"""9.页面大小设置"""
# width, height = 1366, 768
# async def main():
#     browser = await launch(headless=False, args=[f'--window-size={width},{height}'])
#     page = await browser.newPage()
#     await page.setViewport({'width': width, 'height': height})
#     await page.evaluateOnNewDocument('Object.defineProperties(navigator, {webdriver:{get:()=>undefined}})')
#     await page.goto("https://antispider1.scrape.center/")
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

"""10.用户数据持久化"""
# async def main():
#     browser = await launch(headless=False, userDataDir='./userdata')
#     page = await browser.newPage()
#     await page.goto('https://www.bilibili.com/')
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

"""11.Browser"""
# async def main():
#     browser = await launch(headless=False, userDataDir='./userdata')
#     print(browser)
#
# asyncio.get_event_loop().run_until_complete(main())

"""12.开启无痕模式"""
# width, height = 1200, 768
# async def main():
#     browser = await launch(headless=False, args=[f'--window-size={width}, {height}'])
#     context = await browser.createIncognitoBrowserContext()
#     page = await context.newPage()
#     await page.setViewport({'width': width, 'height': height})
#     await page.goto('https://www.baidu.com/')
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

"""13.关闭"""
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://www.bilibili.com/')
#     # await asyncio.sleep(100)
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())

"""14.Page"""
# 选择器
# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto("https://spa2.scrape.center/")
#     await page.waitForSelector(".item .name")
#     j_result1 = await page.J(".item .name")
#     j_result2 = await page.querySelector(".item .name")
#     jj_result1 = await page.JJ(".item .name")
#     jj_result2 = await page.querySelectorAll(".item .name")
#     print("J Result1:", j_result1)
#     print("J Result2:", j_result2)
#     print("JJ Result1:", jj_result1)
#     print("JJ Result2:", jj_result2)
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())

# 选项卡操作
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://www.baidu.com')
#     page = await browser.newPage()
#     await page.goto("https://www.bing.com")
#     pages = await browser.pages()
#     print("Pages:", pages)
#     page1 = pages[1]
#     await page1.bringToFront()
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

# 页面操作
# 遇到bug1: page.pdf()和screenshot()方法必须传入路径
# 遇到bug2: 执行完page.goForward()方法后——超时报警Navigation Timeout Exceeded: 60000 ms exceeded.
# 将网站page.goto("https://spa2.scrape.center/") 换成page.goto("https://www.jd.com/")居然不报警了

# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto("https://www.baidu.com/")
#     # await page.goto("https://spa2.scrape.center/")
#     await page.goto("https://www.jd.com/")
#     await asyncio.sleep(5)
#     # 后退
#     await page.goBack()
#     await asyncio.sleep(5)
#     # 前进
#     # await page.goForward()
#     # 运行js代码检查是否有可前进的历史记录
#     can_go_forward = await page.evaluate("() => window.history.length > 1")
#     if can_go_forward:
#         await page.goForward()
#     else:
#         print("无法前进：无历史记录")
#     print("页面前进完成。。。")
#     # 刷新
#     await page.reload()
#     # 保存 PDF
#     await page.pdf({'path': 'example.pdf'})
#     # 截图
#     await page.screenshot({'path': 'example.png'})
#     # 设置页面HTML
#     await page.setContent("<h2>Hello World</h2>")
#     # 设置 User-Agent
#     await page.setUserAgent('Python')
#     # 设置Headers
#     await page.setExtraHTTPHeaders(headers={})
#     # 关闭
#     await page.close()
#     await browser.close()

# asyncio.get_event_loop().run_until_complete(main())

# 点击
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto("https://spa2.scrape.center/")
#     await asyncio.sleep(5)
#     await page.waitForSelector('.item .name')
#     await page.click('.item .name', option={
#         'button': 'right',
#         'clickCount': 1,
#         'delay': 3000,
#     })
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())

# 输入文本

# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto("https://www.taobao.com")
#     # 后退
#     await page.type("#q", 'iPad')
#     # 关闭
#     await asyncio.sleep(10)
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())

# 获取信息
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto("https://spa2.scrape.center/")
#     print('HTML', await page.content())
#     print("Cookies:", await page.cookies())
#     await browser.close()
# asyncio.get_event_loop().run_until_complete(main())


# 执行
width, height = 1366, 768
async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto("https://spa2.scrape.center/")
    await page.waitForSelector(".item .name")
    await asyncio.sleep(5)
    await page.screenshot(path='example.png')
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')

    print(dimensions)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())


# 延时等待
