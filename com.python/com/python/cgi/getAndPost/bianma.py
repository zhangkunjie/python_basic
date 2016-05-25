#!D:\Program Files\Python\python.exe
import io
import sys
print ('Content-type: text/plain;\n\n')
print("hello word!张三")
print(sys.stdout.encoding)
"""
这个函数可以改变ptyhon的sys.stdout的输出编码
"""
def set_output_encoding(codec, errors='strict'):
    sys.stdout = io.TextIOWrapper(
        sys.stdout.detach(), errors=errors,
        line_buffering=sys.stdout.line_buffering)
set_output_encoding('gbk')
print(sys.stdout.encoding)
print("hello word!张三")
