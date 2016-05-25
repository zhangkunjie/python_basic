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
所以在输出完头文件之后，必须flush
"""
sys.stdout.flush()
file = open("D://abc.pdf",'rb')
"""
sys.stdout.buffer.write:输出的是二进制文件
sys.stdout.write输出的是字符串文件，这里必须使用sys.stdout.buffer.write
"""
"""
一次性输出，处理小文件比较合适
特别注意：sys.stdout.buffer.write的参数是字节，不是字符
"""
sys.stdout.buffer.write(file.read())
#sys.stdout.flush()
file.close()