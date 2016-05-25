#!D:\Program Files\Python\python.exe
# coding=utf-8
"""
向客户端设置cookie
语法：Set-cookie:name=name;expires=date;path=path;domain=domain;secure 
注意：最后以两个换行表示头部结束
cookie会存储在客户端中，当客户端再次请求服务器的时候，在header中自动的带上自己的cookie
服务器据此就可以判断是谁在登陆系统，从而根据该客户以往的浏览记录给其推荐产品
注意：session作为客户的主键用于确定唯一客户
"""

import random
import time

"""
使用时间戳作为sesssionId
"""
SessionId=str(int(time.time()))
print ("Set-Cookie:SessionId="+SessionId+";")
print ("Set-Cookie:UserID=zhangsan;")
print ("Set-Cookie:Password=z198861;")
print ("Set-Cookie:Expires=TSaturday, 15-8-2015 23:12:40 GMT;")
print ("Set-Cookie:Domain=http://localhost;")
print ("Set-Cookie:Path=F://cookie;\r\n")
print ("Content-type:text/html\r\n\r\n")

