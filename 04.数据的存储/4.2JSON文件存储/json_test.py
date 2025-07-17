import json

"""2.读取JSON"""
# str = """
# [{
#     "name": "Bob",
#     "gender": "male",
#     "birthday": "1992-10-18"
# }, {
#     "name": "Selina",
#     "gender": "female",
#     "birthday": "1995-10-18"
# }]
# """
#
# print(type(str))
# data = json.loads(str)
# print(data)
# print(type(data))
# 第一种写法
# with open('data.json', encoding='utf-8') as file:
#     str1 = file.read()
#     data = json.loads(str1)
#     print(data)

# 第二种写法
# data2 = json.load(open('data.json', encoding='utf-8'))
# print(data2)

"""3.输出JSON"""
#
# data = [{
#     "name": "Bob",
#     "gender": "male",
#     "birthday": "1992-01-01"
# }]
# with open('data1.json', 'w') as f:
#     f.write(json.dumps(data))

# 添加缩进参数 indent
# data = [{
#     "name": "Bob",
#     "gender": "male",
#     "birthday": "1992-01-01"
# }]
# with open('data1.json', 'w') as f:
#     f.write(json.dumps(data, indent=2))

# 添加中文编码 ensure_ascii=False
data = [{
    "name": "王伟",
    "gender": "男",
    "birthday": "1992-01-01"
}]
with open('data1.json', 'w') as f:
    f.write(json.dumps(data, indent=2, ensure_ascii=False))
