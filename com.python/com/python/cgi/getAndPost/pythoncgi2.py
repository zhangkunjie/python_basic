#!D:\Program Files\Python\python.exe
# coding=utf-8
"""
客户端使用get方式传递参数，服务端接收客户端传递过来的参数并输出给客户端
乱码问题：需要在系统环境变量中新建：PYTHONIOENCODING  utf8
或者试试这个函数：改变sys.stdout的输出编码
def set_output_encoding(codec, errors='strict'):
    sys.stdout = io.TextIOWrapper(
        sys.stdout.detach(), errors=errors,
        line_buffering=sys.stdout.line_buffering)

set_output_encoding('gbk')
"""
import cgi
import io
import sys


 # 创建 FieldStorage 的实例化
form = cgi.FieldStorage()  
name = form.getvalue('name')
age= form.getvalue('age')
print('Content-Type: text/html; charset=utf-8;\n\n')
print("&&&&&&&&&&&&&"+str(sys.stdout.encoding)+"******")
print('<html><body><pre>' + sys.stdout.encoding + '</pre><body></html>')
print("客户端发送给服务器的name=%s"%name)
print("客户端发送给服务器的age=%s"%age)
print('</body></html>')
