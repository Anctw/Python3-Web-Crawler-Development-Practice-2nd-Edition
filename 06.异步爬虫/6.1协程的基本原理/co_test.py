import requests
import asyncio
import aiohttp
import logging
import time

"""1.案例引入"""
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s:%(message)s')
# TOTAL_NUMBER = 3
# URL = 'https://www.httpbin.org/delay/5'
#
# start_time = time.time()
# for i in range(1, TOTAL_NUMBER + 1):
#     logging.info('scraping %s', URL)
#     response = requests.get(URL)
#
# end_time = time.time()
# logging.info('total time %s seconds', end_time - start_time)

"""2.基础知识"""

"""3.协程的用法"""

"""4.准备工作"""

"""5.定义协程"""

# 第一种写法
# async def execute(x):
#     print('Number:', x)
#
#
# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# print('After calling loop')
# 第二种写法
# async def execute(x):
#     print('Number:', x)
#     return x
#
# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')
#
# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# print('Task:', task)
# loop.run_until_complete(task)
# print('Task:', task)
# print('After calling loop')

# 第三种写法
# async def execute(x):
#     print('Number:', x)
#     return x
#
# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')
#
# task = asyncio.ensure_future(coroutine)
# print('Task:', task)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('Task:', task)
# print('After calling loop')

"""6.绑定回调"""

# 第一
# async def request():
#     url = 'https://www.baidu.com'
#     status = requests.get(url)
#     return status
#
#
# def callback(task):
#     print('Status:', task.result())
#
#
# coroutine = request()
# task = asyncio.ensure_future(coroutine)
# task.add_done_callback(callback)
# print('Task:', task)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('Task:', task)

# 第二
# async def request():
#     url = 'https://www.baidu.com'
#     status = requests.get(url)
#     return status
#
#
# coroutine = request()
# task = asyncio.ensure_future(coroutine)
# print('Task:', task)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('Task:', task)
# print('Task Result:', task.result())

"""7.多任务协程"""

# async def request():
#     url = 'https://www.baidu.com'
#     status = requests.get(url)
#     return status
#
# tasks = [asyncio.ensure_future(request()) for _ in range(5)]
# print("Task:", tasks)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# for task in tasks:
#     print('Task Result:', task.result())


"""8.协程实现"""

# 第一
# start = time.time()
#
#
# async def request():
#     url = 'https://www.httpbin.org/delay/5'
#     print("Waiting for", url)
#     response = requests.get(url)
#     print('Get response from', url, 'response', response)
#
# tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# end = time.time()
# print('Cost time:', end - start)

# 第二
# start = time.time()
#
#
# async def get(url):
#     return requests.get(url)
#
#
# async def request():
#     url = 'https://www.httpbin.org/delay/5'
#     print("Waiting for", url)
#     response = await get(url)
#     print('Get response from', url, 'response', response)
#
#
# tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# end = time.time()
# print('Cost time:', end - start)

"""9.使用aiohttp"""


# 第一
# start = time.time()
#
#
# async def get(url):
#     session = aiohttp.ClientSession()
#     response = await session.get(url)
#     await response.text()
#     await session.close()
#     return response
#
#
# async def request():
#     url = 'https://www.httpbin.org/delay/5'
#     print('Waiting for', url)
#     response = await get(url)
#     print('Get response from', url, 'response', response)
#
# tasks = [asyncio.ensure_future(request()) for _ in range(10)]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# end = time.time()
# print('Cost time:', end - start)


# 第二
def test(number):
    start = time.time()

    async def get(url):
        session = aiohttp.ClientSession()
        response = await session.get(url)
        await response.text()
        await session.close()
        return response

    async def request():
        url = 'https://www.baidu.com/'
        await get(url)

    tasks = [asyncio.ensure_future(request()) for _ in range(number)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print('Number', number, 'Cost time:', end - start)


for number in [1, 3, 5, 10, 15, 30, 50, 75, 100]:
    test(number)
