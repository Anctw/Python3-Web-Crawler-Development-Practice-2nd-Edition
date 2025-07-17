from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
from urllib import request
import socks
import socket
import requests

"""2.urllib的代理设置"""
# 第一段代码 使用clash开启的代理(代码成功运行)
# proxy = '127.0.0.1:7890'
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

# 第二段代码  使用clash开启的代理(代码成功运行)
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

# 第三段代码 需要开启SOCKS代理(代理开启失败)
# socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 7891)
# socket.socket = socks.socksocket
# try:
#     response = request.urlopen('https://httpbin.org/get')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

"""3.requests的代理设置"""
# proxy = '127.0.0.1:7890'
# proxies = {
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy
# }
# try:
#     response = requests.get('https://www.httpbin.org/get', proxies=proxies)
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print("运行失败Error", e.args)

"""4.httpx的代理设置"""
"""5.Selenium的代理设置"""
"""6.aiohttp的代理设置"""
"""7.Pyppeteer的代理设置"""
"""8.Playwright的代理设置"""
