import pika
import requests
import pickle

"""3.基本使用"""
# QUEUE_NAME = 'scrape'
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# channel.queue_declare(queue=QUEUE_NAME)
#
#
# def callback(ch, method, properties, body):
#     print(f"Get {body}")
#
#
# channel.basic_consume(queue='scrape', auto_ack=True, on_message_callback=callback)
# channel.start_consuming()

"""4.随用随取"""
# QUEUE_NAME = 'scrape'
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
# # channel.queue_declare(queue=QUEUE_NAME)
# while True:
#     input()
#     method_frame, header, body = channel.basic_get(
#         queue=QUEUE_NAME, auto_ack=True)
#     if body:
#         print(f'Get {body}')

"""5.优先级队列"""
"""6.队列持久化"""
"""7.实战"""
MAX_PRIORITY = 100
QUEUE_NAME = 'scape_queue'
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
session = requests.Session()


def scrape(request):
    try:
        response = session.send(request.prepare())
        # print(request.prepare())
        # print(response.text)
        print(f'success scraped {response.url}')
    except requests.RequestException:
        print(f'error occurred when scraping {request.url}')


while True:
    method_frame, header, body = channel.basic_get(
        queue=QUEUE_NAME, auto_ack=True)
    if body:
        request = pickle.loads(body)
        print(f'Get {request}')
        scrape(request)
