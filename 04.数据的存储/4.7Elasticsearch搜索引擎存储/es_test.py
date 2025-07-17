from elasticsearch import Elasticsearch
import json
# 书中的一些API已经过时了
"""4.创建索引"""
# es = Elasticsearch(['http://localhost:9200'])
# result = es.indices.create(index="news", ignore=400)
# print(result)

"""5.删除索引"""
# result = es.indices.delete(index="news", ignore=[400, 404])
# print(result)

"""6.插入数据"""
# es = Elasticsearch(['http://localhost:9200'])
# es.indices.create(index="news", ignore=400)
# data = {
#     'title': '乘风破浪不负韶华，奋斗青春圆梦高考',
#     'url': 'https://view.inews.qq.com/a/HEJ2032090439204903'
# }
# result = es.create(index="news", id='1', body=data)
# print(result)

"""7.更新数据"""
# es = Elasticsearch(['http://localhost:9200'])
# data = {
#     'title': '直捣破浪不负韶华，奋斗青春圆梦高考',
#     'url': 'https://view.inews.qq.com/a/HEJ2032090439204903'
# }
# update()方法报错 BadRequestError(400, 'x_content_parse_exception', '[1:2] [UpdateRequest] unknown field [title]'
# result = es.update(index="news", body=data, id=1)
# result = es.index(index="news", body=data, id=1)
# print(result)

"""8.删除数据"""
# es = Elasticsearch(['http://localhost:9200'])
# result = es.delete(index="news",  id=1)
# print(result)

"""9.查询数据"""
es = Elasticsearch(['http://localhost:9200'])
# mapping = {
#     'properties': {
#         'title': {
#             'type': 'text',
#             'analyzer': 'ik_max_word',
#             'search_analyzer': 'ik_max_word'
#         }
#     }
# }
# es.indices.delete(index='news', ignore=[400, 404])
# es.indices.create(index='news', ignore=400)
# result = es.indices.put_mapping(index='news', body=mapping)
# print(result)

# 插入数据
# datas = [
#     {
#         'title': '高考结局大不同',
#         'url': 'https://view.inews.qq.com/a/HEJ2032090439204903'
#     },
#     {
#         'title': '进入职业大洗牌时代,“吃香”职业还吃香吗?',
#         'url': 'https://new.qq.com/omn/20210828/20210828A025LK00.html'
#     },
#     {
#         'title': '乘风破浪不负韶华,奋斗青春圆梦高考',
#         'url': 'https://view.inews.qq.com/a/EDU2021041600732200',
#     },
#     {
#         'title': '他,活出了我们理想的样子',
#         'url': 'https://new.qq.com/omn/20210821/20210821A020ID00.html',
#     }
# ]
# for data in datas:
#     es.index(index='news', body=data)

# 打印所有数据
# result = es.search(index='news')
# print(result)

# 进行数据检索
dsl = {
    'query': {
        'match': {
            'title': '高考 圆梦'
        }
    }
}
result = es.search(index='news', body=dsl)
print(result)
