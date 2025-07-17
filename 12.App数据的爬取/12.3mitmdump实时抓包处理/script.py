"""1.实例引入"""
# def request(flow):
#     flow.request.headers['User-Agent'] = 'MitmProxy'
#     print(flow.request.headers)

"""2.日志输入"""
# from mitmproxy import ctx

# def request(flow):
#     flow.request.headers['User-Agent'] = 'MitmProxy'
#     ctx.log.info(str(flow.request.headers))
#     ctx.log.warn(str(flow.request.headers))
#     ctx.log.error(str(flow.request.headers))

"""3.请求"""
from mitmproxy import ctx

# def request(flow):
#     request = flow.request
#     info = ctx.log.info
#     info(request.url)
#     info(str(request.headers))
#     info(str(request.cookies))
#     info(request.host)
#     info(request.method)
#     info(str(request.port))
#     info(request.scheme)


# def request(flow):
#     url = 'https://www.baidu.com'
#     flow.request.url = url

"""4.响应"""
# def response(flow):
#     response = flow.response
#     info = ctx.log.info
#     info(str(response.status_code))
#     info(str(response.headers))
#     info(str(response.cookies))
#     info(str(response.text))

"""5.实战准备"""

"""6.抓取分析"""


def response(flow):
    print(flow.request.url)
    print(flow.response.text)
