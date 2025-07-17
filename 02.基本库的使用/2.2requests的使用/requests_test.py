"""2.实例引入"""
from requests.auth import HTTPBasicAuth

# import requests
#
# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text[:100])
# print(r.cookies)
#
# print("---------------------------------------")
#
# r1 = requests.get('https://www.httpbin.org/get')
# r2 = requests.post('https://www.httpbin.org/post')
# r3 = requests.put('https://www.httpbin.org/put')
# r4 = requests.delete('https://www.httpbin.org/delete')
# r5 = requests.patch('https://www.httpbin.org/patch')
# print(r1.status_code)
# print(r2.status_code)
# print(r3.status_code)
# print(r4.status_code)
# print(r5.status_code)


"""3.get请求"""

# import requests
# r = requests.get('https://www.httpbin.org/get')
# print(r.text)

# data = {
#     'name': 'germey',
#     'age': 25
# }
# r = requests.get('https://www.httpbin.org/get', params=data)
# print(r.text)

# r = requests.get('https://www.httpbin.org/get')
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

# import re
# r = requests.get('https://ssr1.scrape.center/')
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)

# 抓取二进制数据
# r = requests.get('https://scrape.center/favicon.ico')
# print(r.text)
# print(r.content)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

# 添加请求头
# header = {
#     'User-Agent': 'Mozilla/5.0 '
# }
# r = requests.get('https://ssr1.scrape.center/', headers=header)
# print(r.text)

"""4.POST请求"""
# import requests
# data = {'name':'germey', 'age' : '25'}
# r = requests.post("https://www.httpbin.org/post", data=data)
# print(r.text)

"""5.响应"""
# import requests
# r = requests.get('https://ssr1.scrape.center')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)

"""6.高级用法"""
import requests
# from requests import cookies
# 文件上传
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('https://httpbin.org/post', files=files)
# print(r.text)

# Cookies设置
# TODO 无法实现成功登录
# cookies_str = "_octo=GH1.1.1109115723.1743126150; cpu_bucket=lg; preferred_color_mode=light; tz=Asia%2FShanghai; GHCC=Required:1-Analytics:1-SocialMedia:1-Advertising:1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=missingns"
# jar = requests.cookies.RequestsCookieJar()
# headers = { 'User-Agent': 'Mozilla/5.0'}
# for cookie in cookies_str.split(';'):
#     key, value = cookie.split('=', 1)
#     jar.set(key, value)
# r = requests.get("https://github.com/missingns", cookies=jar, headers=headers)
#
# with open('1.html', 'w' , encoding='utf-8') as f:
#     f.write(r.text)

# Session劫持
# requests.get('https://www.httpbin.org/cookies/set/number/123456789')
# r = requests.get('https://www.httpbin.org/cookies')
# print(r.text)

# s = requests.Session()
# s.get('https://www.httpbin.org/cookies/set/number/123456789')
# r = s.get('https://www.httpbin.org/cookies')
# print(r.text)


# SSL证书验证
# from requests.packages import urllib3
# # urllib3.disable_warnings()
# # response = requests.get('https://expired.badssl.com/' , verify=False)
# # print(response.status_code)


# 身份认证
# from requests.auth import HTTPBasicAuth
# r = requests.get('https://ssr3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
# print(r.status_code)

# 代理设置
# 理论代码，不可实现
# proxies = {'https': 'http://user:password@10.10.10.10:1080/',}
# requests.get('https://www.httpbin.org/get', proxies=proxies)

# Prepared Request
from requests import Request, Session

url = 'https://www.httpbin.org/post'
data = {'name': 'germey'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)


