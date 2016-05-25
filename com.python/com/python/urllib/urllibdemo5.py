#encoding:UTF-8
"""
urllib方式:post方式提交数据
注意：参数data是字节数组类型的，不是字符型的
"""
from urllib.parse import urlencode
import urllib.request


url='http://www.douban.com/tag/2015/movie'
headers= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding':'gzip, deflate',
'Connection':'keep-alive',
'Referer':'http://www.douban.com'
}
data = {'name': '王三',"age":19}
body = urlencode(data).encode(encoding='utf_8', errors='strict')
req = urllib.request.Request("http://localhost/cgi-bin/pythoncgi2.py",method="POST",data=body,headers=headers)
response = urllib.request.urlopen(req)
content = response.read()
print(response.status)
content = content.decode('utf-8')
print(content)

