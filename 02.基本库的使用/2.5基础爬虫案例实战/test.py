import requests
import time
import re

html = requests.get('https://ssr1.scrape.center/detail/1').text
start = time.time()

# print(html)
cover = re.search('class="item.*?<img.*?src="(.*?)".*?class="cover">', html, re.S).group(1).strip()
# cover = re.search('class="item[^"]*".*?<img[^>]*src="([^"]+)"', html, re.S).group(1).strip()
name = re.search('<h2.*?>(.*?)</h2>', html, re.S).group(1).strip()
categories = re.findall('<button.*?category.*?<span>(.*?)</span>.*?</button>', html, re.S)
published_at = re.search('(\d{4}-\d{2}-\d{2})\s?上映', html, re.S).group(1)
drama = re.search('<div.*?drama.*?>.*?<p.*?>(.*?)</p>', html, re.S).group(1).strip()
score = re.search('<p.*?score.*?>(.*?)</p>', html, re.S).group(1).strip()
print(cover)
print(name)
print(categories)
print(published_at)
print(drama)
print(score)
print()
print("耗时:", time.time() - start, "秒")


