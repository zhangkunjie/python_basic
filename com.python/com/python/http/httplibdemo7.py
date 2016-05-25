# coding=UTF-8
import httplib2
"""
如果需要下载的是附件，不需要解码，直接输出到指定文件夹即可
一部分一部分的写，多用来读取大文件
"""
h = httplib2.Http()
url="http://localhost/abc.pdf"
resp, content = h.request(url,method="GET")
out=open("D://mymovie.pdf", "wb")
while True:
    data=content.read(1024)
    out.write(data)
    if not data:
        break
out.close() 