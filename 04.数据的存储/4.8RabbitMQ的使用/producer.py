import pika
import requests
import pickle
"""3.基本使用"""
# QUEUE_NAME = 'scrape'
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# channel.queue_declare(queue=QUEUE_NAME)
# channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body='Hello World!')

"""4.随用随取"""
# QUEUE_NAME = 'scrape'
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# channel.queue_declare(queue=QUEUE_NAME)
# while True:
#     data = input()
#     channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=data)
#     print(f'Put {data}')

"""5.优先级队列"""
# MAX_PRIORITY = 100
# QUEUE_NAME = 'scrape'
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# # 先删除原来的同名无权重的队列
# channel.queue_delete(queue='scrape')
# channel.queue_declare(queue=QUEUE_NAME, arguments={'x-max-priority': MAX_PRIORITY})
# while True:
#     data, priority = input().split()
#     channel.basic_publish(exchange='', routing_key=QUEUE_NAME,
#                           properties=pika.BasicProperties(priority=int(priority)),
#                           body=data)
#     print(f'Put {data}')


"""6.队列持久化"""
# MAX_PRIORITY = 100
# QUEUE_NAME = 'scrape'
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# # 先删除原来的同名无权重的队列
# channel.queue_delete(queue='scrape')
# channel.queue_declare(queue=QUEUE_NAME, arguments={'x-max-priority': MAX_PRIORITY}, durable=True)
# while True:
#     data, priority = input().split()
#     channel.basic_publish(exchange='', routing_key=QUEUE_NAME,
#                           properties=pika.BasicProperties(
#                               priority=int(priority),
#                               delivery_mode=2),
#                           body=data)
#     print(f'Put {data}')

"""7.实战"""
MAX_PRIORITY = 100
TOTAL = 100
QUEUE_NAME = 'scape_queue'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)

for i in range(1, TOTAL+1):
    url = f'https://ssr1.scrape.center/detail/{i}'
    request = requests.Request('GET', url)
    # print(request)
    channel.basic_publish(exchange='',routing_key=QUEUE_NAME,
                          properties=pika.BasicProperties(),
                          body=pickle.dumps(request))
    print(f'Put request of {url}')











