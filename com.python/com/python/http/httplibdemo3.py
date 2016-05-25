# coding=UTF-8
import urllib.parse
import httplib2
"""
伪装浏览器
method="GET"为默认值，写不写都可以
"""
h = httplib2.Http(".cache")
headers= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding':'gzip, deflate',
'Connection':'keep-alive',
'Referer':'http://www.douban.com'
}
url="http://www.douban.com/tag/2015/movie"
resp, content = h.request(url,method="GET",headers=headers)
print(resp.status)
content = content.decode('UTF-8')
print(content)
