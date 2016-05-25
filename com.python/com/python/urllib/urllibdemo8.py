
#encoding:UTF-8
import urllib.request
"""
如果需要下载的是附件，不需要解码，直接输出到指定文件夹即可
一次性读写:针对小文件比价有效
"""
url="http://localhost/abc.pdf"
content=urllib.request.urlopen(url).read()
#content = content.decode('utf-8')
with open("D://mymovie.pdf", "wb") as code:
     code.write(content)
