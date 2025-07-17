from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
"""2.基本用法"""
# browser = webdriver.Edge()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element(By.ID, 'kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     time.sleep(1000000)
#     # print(browser.page_source)
# finally:
#     browser.close()

"""3.初始化浏览器对象"""
# browser = webdriver.Edge()
# browser = webdriver.Firefox()
# browser = webdriver.Chrome()
# browser = webdriver.Safari()

"""4.访问网页"""
# browser = webdriver.Edge()
# browser.get('https://www.taobao.com')
# print(browser.title)
# time.sleep(1000000)

"""5.查找节点"""
# 单个节点
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element(By.ID, 'q')
# print(input_first)
# browser.close()

# 多个节点
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis = browser.find_elements(By.CSS_SELECTOR, '.sec-cate-content--H5TPjGVS a')
# print(lis)
# browser.close()

"""6.节点交互"""
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input = browser.find_element(By.ID, 'q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# # time.sleep(10000000)
# button = browser.find_element(By.CSS_SELECTOR, '.btn-search')
# button.click()

"""7.动作链"""
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element(By.CSS_SELECTOR, '#draggable')
# target = browser.find_element(By.CSS_SELECTOR, '#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

"""8.运行JavaScript"""
# browser = webdriver.Edge()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

"""9.获取节点信息"""
# 获取属性
# browser = webdriver.Chrome()
# url = 'https://spa2.scrape.center/'
# browser.get(url)
# logo = browser.find_element(By.CLASS_NAME, 'logo-image')
# print(logo)
# print(logo.get_attribute('src'))

# 获取文本值
# browser = webdriver.Chrome()
# url = 'https://spa2.scrape.center/'
# browser.get(url)
# input = browser.find_element(By.CLASS_NAME, 'logo-title')
# print(input.text)

# 获取ID、位置、标签名和大小
# browser = webdriver.Chrome()
# url = 'https://spa2.scrape.center/'
# browser.get(url)
# input = browser.find_element(By.CLASS_NAME, 'logo-title')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

"""10.切换Frame"""
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element(By.CLASS_NAME, 'logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo1 = browser.find_element(By.CLASS_NAME, 'logo')
# print(logo1)
# print(logo1.text)

"""11.延时等待"""
# 隐式等待
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get('https://spa2.scrape.center/')
# input = browser.find_element(By.CLASS_NAME, 'logo-image')
# print(input)

# 显式等待
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)

"""12.前进和后退"""
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.get('https://www.taobao.com')
# browser.get('https://www.python.org')
# browser.back()
# time.sleep(100)
# browser.forward()
# browser.close()

"""13.Cookie"""
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

"""14.选项卡管理"""
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to.window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to.window(browser.window_handles[0])
# browser.get('https://python.org')

"""15.异常处理"""
# 示例1
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.find_element(By.ID, 'hello')

# 示例2
# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
# except TimeoutException:
#     print('Time Out')
# try:
#     browser.find_element(By.ID, 'hello')
# except NoSuchElementException:
#     print('No Element')
# finally:
#     browser.close()

"""16.反屏蔽"""
# browser = webdriver.Chrome()
# browser.get('https://antispider1.scrape.center')
# time.sleep(1000)

# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# option.add_experimental_option('useAutomationExtension', False)
# browser = webdriver.Chrome(options=option)
# browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
#     'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined })'
# })
# browser.get('https://antispider1.scrape.center')
# time.sleep(1000)

"""17.无头模式"""
# option = ChromeOptions()
# option.add_argument('--headless')
# browser = webdriver.Chrome(options=option)
# browser.get('https://www.baidu.com')
# browser.get_screenshot_as_file('preview.png')
