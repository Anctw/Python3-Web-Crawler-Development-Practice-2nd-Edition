import pymysql

"""2.连接数据库"""
# db = pymysql.connect(host='localhost', user='root', passwd='root', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8mb4")
# db.close()

"""3.创建表"""
# db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

"""4.插入数据"""
# id = '20120001'
# user = 'Bob'
# age = 20
#
# db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
# cursor = db.cursor()
# 插入数据第一种方法
# sql = 'INSERT INTO students(id,name, age) VALUES (%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except EOFError:
#     db.rollback()
# db.close()

# 插入数据第二种方法
# data = {
#     'id': '20120002',
#     'name': 'cvb',
#     'age': 21
# }
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
# sql = 'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# try:
#     if cursor.execute(sql, tuple(data.values())):
#         print('Successful')
#         db.commit()
# except Exception as e:
#     print(sql)
#     print(e)
#     print('Failed')
#     db.rollback()
# db.close()

"""5.更新数据"""
# db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
# cursor = db.cursor()
# sql = "UPDATE STUDENTS SET AGE = %s WHERE NAME = %s"
# try:
#     cursor.execute(sql, (25, 'Bob'))
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()
# db.close()

# 主键存在就修改数据，主键不存在就插入数据
# data = {
#     'id': '20120002',
#     'name': 'cvb',
#     'age': 20
# }
# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
#
# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
# update = ','.join(["{key} = %s".format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values())*2):
#         print(sql)
#         print('Successful')
#         db.commit()
# except Exception as e:
#     print(e)
#     print(sql)
#     print('Failed')
#     db.rollback()
# db.close()

"""6.删除数据"""
# db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
# cursor = db.cursor()
# table = 'students'
# condition = 'age > 27'
#
# sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     print(sql)
#     db.commit()
# except Exception as e:
#     print(e)
#     print(sql)
#     db.rollback()
# db.close()


"""7.查询数据"""
db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()
table = 'students'
condition = 'age > 20'

sql = 'SELECT *  FROM {table} WHERE {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    print(sql)
    print("Count:",cursor.rowcount)
    # one = cursor.fetchone()
    # print("One:",one)
    results = cursor.fetchall()
    print("Results:", results)
    print("Results Type:", type(results))

    db.commit()
except Exception as e:
    print(e)
    print(sql)
    print('Error')
db.close()