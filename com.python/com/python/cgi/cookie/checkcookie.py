#!D:\Program Files\Python\python.exe
# coding=utf-8
import cgi, cgitb
from os import environ
"""
从环境变量中取出cookie数据：可以和服务器的账号密码做对比，如果不符合就强制退出登陆等
"""
print('Content-Type: text/html; charset=utf-8;\n\n') 
if 'HTTP_COOKIE' in environ :
   for cookie in environ['HTTP_COOKIE'].split(';'): 
      key , value = str(cookie).strip().split('=')
      #print(key+"*********"+value)
      if key == "UserID":
         user_id = value
      if key == "Password":
         password = value
print ("User ID  = %s" % user_id)
print ("Password = %s" % password)