from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
from urllib import request
import socks
import socket
import requests
from Demos.win32ts_logoff_disconnected import username
from playwright.sync_api import sync_playwright
import asyncio
import pyppeteer
import aiohttp
from aiohttp_socks import ProxyConnector
import httpx
from httpx_socks import SyncProxyTransport
from httpx_socks import AsyncProxyTransport
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import  zipfile

"""2.urllib的代理设置"""
# 第一段代码 使用clash开启的代理(代码成功运行)
# proxy = '127.0.0.1:7890'
# proxy_header = ProxyHandler({
#     'http': "http://" + proxy,
#     "https": "https://" + proxy
# })
# opener = build_opener(proxy_header)
# try:
#     response = opener.open("https://www.httpbin.org/get")
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print("访问失败：{}".format(e.reason))

# 第二段代码  同上代码成功运行
# proxy = 'username:password@127.0.0.1:7890'
# proxy_header = ProxyHandler({
#     'http': "http://" + proxy,
#     "https": "https://" + proxy
# })
#
# opener = build_opener(proxy_header)
# try:
#     response = opener.open("https://www.httpbin.org/get")
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print("访问失败：{}".format(e.reason))

# 第三段代码 同上代码成功运行
# socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 7890)
# socket.socket = socks.socksocket
# try:
#     response = request.urlopen('https://httpbin.org/get')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

"""3.requests的代理设置"""
# 此代码运行失败
proxy = '127.0.0.1:7890'
proxies = {
    'http': 'http://' + proxy,
    'https': 'http://' + proxy
}
try:
    response = requests.get('https://www.httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print("运行失败Error", e.args)

# SOCKS代理设置方法一 同上代码运行成功
# proxy = '127.0.0.1:7890'
# proxies = {
#     'http': 'socks5://' + proxy,
#     'https': 'socks5://' + proxy
# }
# try:
#     response = requests.get('https://www.httpbin.org/get', proxies=proxies)
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print("运行失败Error", e.args)

# SOCKS代理设置方法二 同上代码运行成功
# socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 7890)
# socket.socket = socks.socksocket
# try:
#     response = requests.get('https://www.httpbin.org/get')
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print("运行失败Error", e.args)


"""4.httpx的代理设置"""
# 无认证的代理 代码运行成功 http可以跑通、https跑不通
# proxy = '127.0.0.1:7890'
# # proxies = {
# #     'http://': 'http://' + proxy,
# #     'https://': 'http://' + proxy,
# # }
# proxy_url = 'http://' + proxy
#
# with httpx.Client(proxy=proxy_url) as client:
#     response = client.get('http://www.httpbin.org/get')
#     print(response.text)


#SOCKS代理 代码运行成功
# transport = SyncProxyTransport.from_url('socks5://127.0.0.1:7890')
#
# with httpx.Client(transport=transport) as client:
#     response = client.get('https://www.httpbin.org/get')
#     print(response.text)

# 异步模式设置 代码成功
# transport = AsyncProxyTransport.from_url('socks5://127.0.0.1:7890')
#
# async def main():
#     async with httpx.AsyncClient(transport=transport) as client:
#         response = await client.get('https://www.httpbin.org/get')
#         print(response.text)
#
# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())

"""5.Selenium的代理设置"""
# 无认证的代理 代码运行成功
# proxy = '127.0.0.1:7890'
# options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=http://' + proxy)
# browser = webdriver.Chrome(options=options)
# browser.get('https://www.httpbin.org/get')
# print(browser.page_source)
# browser.close()

# 需要认证的代理 代码运行成功
# ip = '127.0.0.1'
# port = 7890
# username = 'foo'
# password = 'bar'
#
# manifest_json = """{"version":"1.0.0","manifest_version":2,"name":"Chrome Proxy", "permissions":
#             ["proxy","tabs","unlimitedStorage","storage","<all_urls>","webRequest","webRequestBlocking"],"background":
#             {"scripts":["background.js"]}}"""
#
# background_js = """
# var config = {
#             mode:"fixed_servers",
#             rules:{
#                 singleProxy:{
#                     scheme:"http",
#                     host:"%(ip) s",
#                     port:%(port) s,
#                 }
#             }
#         }
# chrome.proxy.settings.set({value:config, scope:"regular"}, function(){});
#
# function callbackFn(details) {
#     return {
#         authCredentials:{
#             username: "%(username) s",
#             password: "%(password) s",
#             }
#         }
#     }
# chrome.webRequest.onAuthRequired.addListener(
#         callbackFn, {urls: ["<all_urls>"]}, ["blocking"])
#         """ % {'ip':ip, "port": port, 'username':username, 'password':password }
#
# plugin_file = 'proxy_auth_plugin.zip'
# with zipfile.ZipFile(plugin_file, 'w') as zp:
#     zp.writestr("manifest.json", manifest_json)
#     zp.writestr("background.js", background_js)
# options = Options()
# options.add_argument('--start-maximized')
# options.add_extension(plugin_file)
# browser = webdriver.Chrome(options=options)
# browser.get("https://www.httpbin.org/get")
# print(browser.page_source)
# browser.close()

# SOCKS代理 代码运行成功
# proxy = '127.0.0.1:7890'
# options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=socks5://' + proxy)
# browser = webdriver.Chrome(options=options)
# browser.get('https://www.httpbin.org/get')
# print(browser.page_source)
# browser.close()

"""6.aiohttp的代理设置"""
# 第一段代码 同上代码成功运行
# proxy = "http://127.0.0.1:7890"
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://www.httpbin.org/get', proxy=proxy) as response:
#             print(await response.text())
#
# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())

# SOCKS 代码运行失败

# async def main():
#     # 这段代码放在函数中声明
#     connector = ProxyConnector.from_url('socks5://127.0.0.1:7890')
#     async with aiohttp.ClientSession(connector=connector) as session:
#         async with session.get('https://www.httpbin.org/get') as response:
#             print(await response.text())
#
# if __name__ == '__main__':
#     # asyncio.get_event_loop().run_until_complete(main())
#     asyncio.run(main())

"""7.Pyppeteer的代理设置"""
# 第一段代码 同上代码成功运行
# proxy = "127.0.0.1:7890"
#
# async def main():
#     browser = await pyppeteer.launch({'args': ['--proxy-server=http://' + proxy], 'headless': True})
#     page = await browser.newPage()
#     await page.goto('https://www.httpbin.org/get')
#     print(await page.content())
#     await browser.close()
#
# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())

# SOCKS 同上代码成功运行
# proxy = "127.0.0.1:7890"
#
# async def main():
#     browser = await pyppeteer.launch({'args': ['--proxy-server=socks5://' + proxy], 'headless': True})
#     page = await browser.newPage()
#     await page.goto('https://www.httpbin.org/get')
#     print(await page.content())
#     await browser.close()
#
# if __name__ == "__main__":
#     asyncio.get_event_loop().run_until_complete(main())


"""8.Playwright的代理设置"""
# 第一段代码 同上代码成功运行
# with sync_playwright() as p:
#     browser = p.chromium.launch(proxy={'server': 'http://127.0.0.1:7890'})
#     page = browser.new_page()
#     page.goto("https://www.httpbin.org/get")
#     print(page.content())
#     browser.close()

# SOCKS代理 同上代码成功运行
# with sync_playwright() as p:
#     browser = p.chromium.launch(proxy={'server': 'socks5://127.0.0.1:7890'})
#     page = browser.new_page()
#     page.goto("https://www.httpbin.org/get")
#     print(page.content())
#     browser.close()

# 认证的代理 同上代码成功运行
# with sync_playwright() as p:
#     browser = p.chromium.launch(proxy={
#         'server': 'http://127.0.0.1:7890',
#         "username": 'foo',
#         'password': 'bar',})
#     page = browser.new_page()
#     page.goto("https://www.httpbin.org/get")
#     print(page.content())
#     browser.close()