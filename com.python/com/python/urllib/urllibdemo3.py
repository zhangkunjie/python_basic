#encoding:UTF-8
"""
urllib方式抓取数据：伪装浏览器
"""
import urllib.request
url='http://www.douban.com/tag/2015/movie'
headers= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding':'gzip, deflate',
'Connection':'keep-alive',
'Referer':'http://www.douban.com'
}
req = urllib.request.Request(url,method="GET",headers=headers)
response = urllib.request.urlopen(req)
content = response.read()
print(response.status)
content = content.decode('utf-8')
print(content)

