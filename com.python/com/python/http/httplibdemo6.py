# coding=UTF-8
import httplib2
"""
如果需要下载的是附件，不需要解码，直接输出到指定文件夹即可
一次性读取，多用来读取小文件
"""
h = httplib2.Http()
url="http://localhost/abc.pdf"
resp, content = h.request(url,method="GET")
print(resp.status)
with open("D://mymovie.pdf", "wb") as code:
     code.write(content)