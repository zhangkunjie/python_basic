# coding=UTF-8
import httplib2
"""
最简单的网络抓取，没有伪装浏览器
method="GET" 默认值，可以不写
"""
h = httplib2.Http()
url="http://www.douban.com/tag/2014/movie?start=2700"
resp, content = h.request(url,method="GET")
print(resp.status)
content = content.decode('utf-8')
print(content)
