#!D:\Program Files\Python\python.exe
# coding=utf-8
# HTTP Header
import io
import os
import sys


print ("Content-Type:application/octet-stream; name=\"abc.pdf\"")
print ("Content-Disposition: application/octet-stream; filename=\"abc.pdf\"\n\n")
"""
由于输出有缓存，如果不flush，header的信息就会被当做输出文件的一部分，从而破坏了输出文件的结构
"""
sys.stdout.flush()
"""
封装输出流,不使用缓存
"""
file = open("D://abc.pdf",'rb')
sys.out=os.fdopen(sys.stdout.fileno(),"wb",0)
while True:
    data = file.read(1024)
    sys.stdout.buffer.write(data)
    if not data:
        break
file.close()