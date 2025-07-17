import socket
import urllib.request
import urllib.parse
import urllib.error
from urllib import request, parse

"""1.发送请求"""
# 测试urlopen方法
# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
# print(type(response))
# <class 'http.client.HTTPResponse'>

# print(response.msg)
# print(response.getheaders())
# print(response.getheader('content-type'))


# 测试urlopen方法中的data参数
# data = bytes(urllib.parse.urlencode({'name':'germey'}), encoding='utf-8')
# response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))


# 测试urlopen方法中的timeout参数
# response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
# print(response.read())
# urllib.error.URLError: <urlopen error _ssl.c:1112: The handshake operation timed out>
# try:
#     response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')


# 测试Request类进行参数设置
# url = 'https://httpbin.org/post'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (compatible; MISE 5.5; Windows NT)',
#     'Host': 'www.httpbin.org'
# }
# dict = {'name': 'germey'}
# data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))


# 测试HTTPBasicAuthHandler模板完成认证登录
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError
#
# username = 'admin'
# password = 'admin'
# url = 'https://ssr3.scrape.center/'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)


# 使用代理进行爬虫
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:8080',
#     'https': 'https://127.0.0.1:8080'
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com/')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)


# 测试Cookie需要用到相关的Handler
# import http.cookiejar, urllib.request
#
# filename = 'cookie_baidu.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)


"""2.处理异常"""
# 测试URLError异常
# from urllib import request, error
#
# try:
#     response = request.urlopen('https://cuiqingcai.com/404')
# except error.URLError as e:
#     print(e.reason)


# 测试HTTPError异常
# from urllib import request, error

# 第一版
# try:
#     response = request.urlopen('https://cuiqingcai.com/404')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')

# 第二版
# try:
#     response = request.urlopen('https://cuiqingcai.com/404')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

# 测试URLError异常中： reason返回对象而不是字符串
# import socket
# import urllib.request
# import urllib.error
# try:
#     response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
# except urllib.error.URLError as e:
#     print(type(e.reason))
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')


"""3.解析链接"""
# 测试urlparse
# from urllib.parse import urlparse
#
# result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
# print(type(result))
# print(result)  # scheme://netloc/path;params?query#fragment
# <class 'urllib.parse.ParseResult'>
# ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')

# 测试urlunparse
# from urllib.parse import urlunparse
# data = ['https', 'www.baidu.com', 'index.html','user', 'a=6', 'comment']
# print(urlunparse(data))

# 测试urlsplit
# from urllib.parse import urlsplit
# result = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
# print(result)

# 测试urlunsplit
# from urllib.parse import urlunsplit
# data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
# print(urlunsplit(data))

# 测试urljoin
# 分析base_url中scheme、netloc、path这3个内容添加到新链接中

# 测试 urlencode： 对字典进行编码
# from urllib.parse import urlencode
#
# params = {
#     'name': 'germey',
#     'age': 25
# }
# base_url = 'https://www.baidu.com'
# url = base_url + '?' + urlencode(params)
# print(url)


# 测试parse_qs
# from urllib.parse import parse_qs
# query = 'name=germey&age=25'
# print(parse_qs(query))

# 测试parse_qsl
# from urllib.parse import parse_qsl
# query = 'name=germey&age=25'
# print(parse_qsl(query))

# 测试quote: 对中文进行编码
# from urllib.parse import quote
# keyword = '笔记'
# url = 'https://www.baidu.com/s?wd=' + quote(keyword)
# print(url)

# 测试unquote 对中文进行解码
# from urllib.parse import unquote
# url = 'https://www.baidu.com/s?wd=%E7%AC%94%E8%AE%B0'
# print(unquote(url))


"""4.分析Robots协议"""
# 测试Robotsparser 第一种
# from urllib.robotparser import RobotFileParser

# rp = RobotFileParser()
# rp.set_url('https://www.baidu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
# print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
# print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))

# 第二种
from urllib.request import urlopen
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.parse(urlopen('https://www.baidu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))






