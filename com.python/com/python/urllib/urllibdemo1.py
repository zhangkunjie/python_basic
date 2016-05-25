#encoding:UTF-8
"""
urllib方式抓取数据：简单抓取
"""
import urllib.request
url="http://www.douban.com/tag/2015/movie"
response=urllib.request.urlopen(url)
print(response.status)
content=response.read()
content = content.decode('utf-8')
print(content)

