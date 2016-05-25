#encoding:UTF-8
"""
urllib方式抓取数据：使用request
"""
import urllib.request
url="http://www.douban.com/tag/2015/movie"
req = urllib.request.Request(url,method="GET")
response = urllib.request.urlopen(req)
content = response.read()
print(response.status)
content = content.decode('utf-8')
print(content)

