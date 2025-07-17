import csv
import pandas
"""1.写入"""
# with open('data.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', '20'])
#     writer.writerow(['10002', 'Bob', '22'])
#     writer.writerow(['10004', 'Jordan', '21'])


# 设置分隔符参数
# with open('data.csv', 'w', newline='') as f:
#     writer = csv.writer(f, delimiter="*")
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', '20'])
#     writer.writerow(['10002', 'Bob', '22'])
#     writer.writerow(['10004', 'Jordan', '21'])

# 调用writerows方法写入多行
# with open('data.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', '20'])
#     writer.writerows([['10002', 'Bob', '22'], ['10003', 'Jordan', '21']])

# 写入字典数据
# with open('data.csv', 'w', newline='') as csvfile:
#     filenames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=filenames)
#     writer.writeheader()
#     writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
#     writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
#     writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

# 追加模式
# with open('data.csv', 'a', newline='') as csvfile:
#     filenames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=filenames)
#     writer.writerow({'id': '10004', 'name': 'Durant', 'age': 28})

# 写入中文数据
# with open('data.csv', 'a', encoding='utf-8', newline='') as csvfile:
#     filenames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=filenames)
#     writer.writerow({'id': '10005', 'name': '王伟', 'age': 18})

# 使用pandas中to_csv方法
# data = [
#     {'id': '10001', 'name': 'Mike', 'age': 20},
#     {'id': '10002', 'name': 'Bob', 'age': 22},
#     {'id': '10003', 'name': 'Jordan', 'age': 21}
# ]
# df = pandas.DataFrame(data)
# df.to_csv('data.csv', index=False)

"""2.读取"""
# 使用Reader对象读取
# with open('data.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)

# 使用pandas中的read_csv方法读取
# df = pandas.read_csv('data.csv')
# print(df)

# 使用pandas中的read_csv方法读取转化为列表
df = pandas.read_csv('data.csv')
for index, row in df.iterrows():
    print(row.tolist())


