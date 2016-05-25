# coding=UTF-8
import urllib.parse
import httplib2
"""
使用缓存
"""
h = httplib2.Http(".cache")
url="http://www.douban.com/tag/2015/movie"
resp, content = h.request(url,method="GET")
print(resp.status)
content = content.decode('UTF-8')
print(content)
