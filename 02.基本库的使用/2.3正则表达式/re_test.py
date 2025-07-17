"""2.match"""
# import re

# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.span())

# 匹配目标
# content = 'Hello 1234567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())

# 通用匹配
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello.*Demo$', content)
# print(result)
# print(result.group())
# print(result.span())


# 贪婪与非贪婪
# .*贪婪   .*?非贪婪
# content = 'Hello 1234567 World_This is a Regex Demo'
# print(len(content))
# # result = re.match('^He.*(\d+).*Demo$', content)
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result)
# print(result.group(1))


# 修饰符
# content = '''Hello 1234567 World_This
# is a Regex Demo'''
# print(len(content))
# result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
# print(result.group(1))


# 转义匹配
# content = '(百度)www.baidu.com'
# result = re.match('\(百度\)www\.baidu\.com', content)
# print(result)

"""3.search"""
# import re
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra    stings'
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result)
# print(result.group(1))

"""4.findall"""
# import re
# html = '''<div id="songs-list">
# <h2 class="title">经典老歌</h2>
# <p class="introduction">
# 经典老歌列表
# </p>
# <ul id="list" class="list-group">
# <li data-view="2">一路上有你</li>
# <li data-view="7">
# <a href="/2.mp3"singer="任贤齐">沧海一声笑</a>
# </li>
# <li data-view="4" class="active">
# <a href="/3.mp3"singer="齐秦">往事随风</a>
# </li>
# <li data-view="6"><a href="/4.mp3"singer="beyond">光辉岁月</a></li>
# <li data-view="5"><a href="/5.mp3"singer="陈慧琳">记事本</a></li>
# <li data-view="5">
# <a href="/6.mp3"singer="邓丽君">但愿人长久</a>
# </li>
# </ul>
# </div>'''
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# # print(results)
# print(type(results))
# for result in results:
#     print(result[0], result[1], result[2])



"""5.sub"""
# import re
# content = '54ak54yr5oiR54ix5L2g'
# content = re.sub('\d+', '', content)
# print(content)


"""6.compile"""
# 将正则表达式字符串编译为正则对象
import re
content1 = '2019-12-15 12:00'
content2 = '2019-12-17 12:55'
content3 = '2019-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)





