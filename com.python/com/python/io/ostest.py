# coding=utf-8
"""
os的一些操作
"""
"""
重命名os.rename(current_file_name, new_file_name)
"""
import os
os.rename( "D://2train.txt", "D://train.txt" )
#删除文件
os.remove("D://train.txt")
#创建文件夹
os.mkdir("D://test2")
#改变当前目录
os.chdir("D://test2")
#显示当前工作目录
print(os.getcwd())
#删除目录
os.rmdir("D://test" )