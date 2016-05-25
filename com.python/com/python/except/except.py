# coding=utf-8
try:
   fh = open("D://t.txt", "r")
except IOError:
   print ("Error:找不到指定文件")
else:
   print ("读取文件成功")
   fh.close()