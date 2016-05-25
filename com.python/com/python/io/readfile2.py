# coding=utf-8
"""
读取文件
"""
#按照指定大小一块一块读取
file_object = open('D://train.txt', 'r')
try:
    while True:
        chunk = file_object.read(100)
        print(chunk)
        if not chunk:
            break
finally:
     file_object.close( )
