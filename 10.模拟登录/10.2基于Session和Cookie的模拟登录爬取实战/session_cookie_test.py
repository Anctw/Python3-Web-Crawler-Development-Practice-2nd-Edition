import requests
import time
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
"""3.模拟登录"""
# 第一段代码
# BASE_URL = 'https://login2.scrape.center/'
# LOGIN_URL = urljoin(BASE_URL, '/login')
# INDEX_URL = urljoin(BASE_URL, '/page/1')
# USERNAME = 'admin'
# PASSWORD = 'admin'
#
# response_login = requests.post(LOGIN_URL, data={
#     'username': USERNAME,
#     'password': PASSWORD
# })
#
# response_index = requests.get(INDEX_URL)
# print('Response Status', response_index.status_code)
# print('Response URL', response_index.url)


# 第二段代码
# BASE_URL = 'https://login2.scrape.center/'
# LOGIN_URL = urljoin(BASE_URL, '/login')
# INDEX_URL = urljoin(BASE_URL, '/page/1')
# USERNAME = 'admin'
# PASSWORD = 'admin'
#
# response_login = requests.post(LOGIN_URL, data={
#     'username': USERNAME,
#     'password': PASSWORD
# }, allow_redirects=False)
#
# cookies = response_login.cookies
# print('Cookies', cookies)
#
# response_index = requests.get(INDEX_URL, cookies=cookies)
# print('Response Status', response_index.status_code)
# print('Response URL', response_index.url)

# 第三段代码
# BASE_URL = 'https://login2.scrape.center/'
# LOGIN_URL = urljoin(BASE_URL, '/login')
# INDEX_URL = urljoin(BASE_URL, '/page/1')
# USERNAME = 'admin'
# PASSWORD = 'admin'
#
# session = requests.Session()
#
# response_login = session.post(LOGIN_URL, data={
#     'username': USERNAME,
#     'password': PASSWORD
# })
#
# cookies = session.cookies
# print('Cookies', cookies)
#
# response_index = session.get(INDEX_URL)
# print('Response Status', response_index.status_code)
# print('Response URL', response_index.url)

# 第四段代码
BASE_URL = 'https://login2.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

browser = webdriver.Chrome()
browser.get(BASE_URL)
browser.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(USERNAME)
browser.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(PASSWORD)
browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
time.sleep(10)

# 从浏览器对象中获取Cookie信息
cookies = browser.get_cookies()
print('Cookies', cookies)
browser.close()

# 把Cookies信息放入到请求中
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])

response_index = session.get(INDEX_URL)
print('Response Status', response_index.status_code)
print('Response URL', response_index.url)
