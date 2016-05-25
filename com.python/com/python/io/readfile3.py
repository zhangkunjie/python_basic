# coding=utf-8
"""
读取文件
"""
#一行一行读取
file_object = open('D://train.txt', 'r')
try:
    while True:
        lines = file_object.readlines()
        for line in lines:
         print(line)
        if not line:
            break
finally:
     file_object.close( )  
