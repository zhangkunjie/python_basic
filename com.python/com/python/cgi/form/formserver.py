#!D:\Program Files\Python\python.exe
# coding=utf-8
import cgi
import io
import sys
 # 创建 FieldStorage 的实例化
form = cgi.FieldStorage()  
print('Content-Type: text/html; charset=utf-8;\n\n')
name = form.getvalue('name')
age= form.getvalue('age')
gender=form.getvalue('gender')
city=form.getvalue('city')
"""
注意：对于多选框这里得到的是一个list列表，需要转换成str后才能输出
"""
hoby=form.getvalue('hoby')
introduction=form.getvalue("introduction")
print("姓名:"+name)
print("年龄:"+age)
print("性别:"+gender)
print("城市:"+city)
print("兴趣爱好:"+str(hoby))
print("个人简介:"+introduction)

