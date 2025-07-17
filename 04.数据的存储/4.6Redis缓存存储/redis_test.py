from redis import StrictRedis, ConnectionPool

"""3.连接Redis"""
# 第一种连接方式
# redis = StrictRedis(host='localhost', port=6379, db=2, password='')
# redis.set('name', 'Bob')
# print(redis.get('name'))

# 第二种连接方式
# pool = ConnectionPool(host='localhost', port=6379, db=2, password='')
# redis = StrictRedis(connection_pool=pool)
# print(redis.get('name'))

# 第三种连接方式（通过URL连接）
# url = 'redis://:@localhost:6379/2'
# pool = ConnectionPool().from_url(url)
# redis = StrictRedis(connection_pool=pool)
# print(redis.get('name'))

"""4.键操作"""

"""5.字符串操作"""

"""6.列表操作"""

"""7.集合操作"""

"""8.有序集合操作"""

"""9.散列操作"""

