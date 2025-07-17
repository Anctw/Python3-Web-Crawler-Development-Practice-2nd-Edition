import pymongo
from bson.objectid import ObjectId
"""2.连接MongoDB"""
# client = pymongo.MongoClient(host='localhost', port=27017)
# 或者
client = pymongo.MongoClient('mongodb://localhost:27017/')
"""3.指定数据库"""
db = client.test
# 等价于 db = client['test']

"""4.指定集合"""
collection = db.stdudents

"""5.插入数据"""
# student = {
#     'id': 20170109,
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# result = collection.insert_one(student)
# print(result)
# print(result.inserted_id)

# 插入多条数据
# student1 = {
#     'id': 20170103,
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
# student2 = {
#     'id': 20170104,
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
# }
# result = collection.insert_many([student1, student2])
# print(result)
# print(result.inserted_ids)

"""6.查询"""
# 查询一条数据
# result = collection.find_one({'name': 'Mike'})
# print(type(result))
# print(result)

# 根据_id查询
# result = collection.find_one({'_id': ObjectId('67ecba22e3ee1fe31265e8b4')})
# print(result)

# 查询多条数据
# results = collection.find({'age': 20})
# print(type(results))
# for result in results:
#     print(result)

# 条件查询
# results1 = collection.find({'age': {'$gt': 20}})
# print(type(results1))
# for result in results1:
#     print(result)
# print("================================================")
# results2 = collection.find({'name': {'$regex': '^M.*'}})
# for result in results2:
#     print(result)

"""7.计数"""
# count()方法已淘汰
# count = collection.count_documents({'age': 20})
# print(count)

"""8.排序"""
# results4 = collection.find().sort('name', pymongo.ASCENDING)
# print([result['name'] for result in results4])

"""9.偏移"""
# results4 = collection.find().sort('name', pymongo.ASCENDING).skip(2)
# print([result['name'] for result in results4])

# results4 = collection.find().sort('name', pymongo.ASCENDING).skip(1).limit(2)
# print([result['name'] for result in results4])

"""10.更新"""
# 对于当前版本update()方法不可用  update_one()方法
# condition = {'name': 'Jordan'}
# student = collection.find_one(condition)
# student['age'] = 25
# result = collection.update_one(condition, {'$set': student})
# print(result)
# print(result.matched_count, result.modified_count)

# update_many()方法
# condition = {'age': {'$gt': 20}}
# result = collection.update_many(condition, {'$inc': {'age': 1}})
# print(result)
# print(result.matched_count, result.modified_count)


"""11.删除"""
# 对于当前版本remove()方法不可用  delete_one()方法
# result = collection.delete_one({'name': 'Asdhjs'})
# print(result)

# delete_many()方法
result = collection.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)






