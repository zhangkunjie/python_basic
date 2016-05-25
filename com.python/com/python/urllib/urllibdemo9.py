
#encoding:UTF-8
import urllib.request
"""
如果需要下载的是附件，不需要解码，直接输出到指定文件夹即可
一部分一部分的写文件，多用来读取大文件
"""
url="http://localhost/abc.pdf"
content=urllib.request.urlopen(url).read()
out=open("D://mymovie.pdf", "wb")
while True:
    data=content.read(1024)
    out.write(data)
    if not data:
        break
out.close()    
    