#!D:\Program Files\Python\python.exe
# coding=utf-8
# HTTP Header
import io
import os
import sys


print ("Content-Type:application/octet-stream; name=\"abc.pdf\"")
print ("Content-Disposition: application/octet-stream; filename=\"abc.pdf\"\r\n\n")
"""
由于输出有缓存，如果不flush，header的信息就会被当做输出文件的一部分，从而破坏了输出文件的结构
"""
sys.stdout.flush()
"""
封装输出流,不使用缓存
"""
with io.open(sys.stdout.fileno(),"wb") as fout:
    with open("D://abc.pdf","rb") as fin:
        while True:
            data = fin.read(4096)
            fout.write(data)
            if not data:
                break
