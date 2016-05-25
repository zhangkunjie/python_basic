# coding=UTF-8
import urllib
import httplib2
"""
提交数据:post方式，注意服务器端肯会有乱码：
method：默认值为get,这里得修改为post
"""
from urllib.parse import urlencode
h = httplib2.Http(".cache")
headers= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding':'gzip, deflate',
'Connection':'keep-alive',
'Referer':'http://www.douban.com'
}
data = {'name': '王六',"age":22}
body = urlencode(data)
resp, content = h.request("http://localhost/cgi-bin/pythoncgi2.py", method="POST", body=body,headers=headers)
print(resp.status)
content = content.decode('utf-8')
print(content)