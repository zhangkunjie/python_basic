#!D:\Program Files\Python\python.exe
# coding=utf-8
# HTTP Header
import io
import os
import sys
print ("Content-Type:application/octet-stream; name=\"abc.pdf\"")
print ("Content-Disposition: application/octet-stream; filename=\"abc.pdf\"\r\n\n")
sys.stdout.flush()
file = open("D://abc.pdf",'rb')
"""
一块一块的读取输出，主要针对大文件
"""
while True:
    data = file.read(1024)
    """
        这里使用buffer.write用来输出字节流,注意是字节流！不是字符
    """
    sys.stdout.buffer.write(data)
    sys.stdout.flush()
    if not data:
        break
sys.stdout.flush()    
file.close()