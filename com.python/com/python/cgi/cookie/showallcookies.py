#!D:\Program Files\Python\python.exe
# coding=utf-8
"""
从环境变量中取出所有的cookie打印
"""
import cgi, cgitb
from os import environ
import os
print ("Content-type: text/plain\n")
if "HTTP_COOKIE" in os.environ:
    for cookie in environ['HTTP_COOKIE'].split(';'): 
        print(cookie)
else:
    print ("没有任何cookie")