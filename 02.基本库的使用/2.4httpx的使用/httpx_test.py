"""1.示例"""
# import requests
# url = 'https://spa16.scrape.center/'
# response = requests.get(url)
# print(response.text)


"""3.基本使用"""
# import httpx

# response = httpx.get('https://httpbin.org/get')
# print(response.status_code)
# print(response.headers)
# print(response.text)

# client = httpx.Client(http2=True)
# response = client.get('https://spa16.scrape.center/')
# print(response.status_code)


"""4.Client对象"""
# import httpx
# url = 'http://www.httpbin.org/headers'
# headers = {'User-Agent': 'myapp/0.0.1'}
# with httpx.Client(headers=headers) as client:
#     r = client.get(url)
#     print(r.json()['headers']['User-Agent'])


"""5.支持HTTP/2.0"""
# import httpx
# client = httpx.Client(http2=True)
# response = client.get('https://www.httpbin.org/get')
# print(response.text)
# print(response.http_version)


"""6.支持异步请求"""
import httpx
import asyncio


async def fetch(url):
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(url)
        print(response.text)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(fetch('https://www.httpbin.org/get'))
