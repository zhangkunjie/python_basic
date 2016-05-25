#!D:\Program Files\Python\python.exe
# coding=utf-8
import cgi
import os
"""
输出文件之前必须设置文件头
"""
print("Content-Type: text/html\n")
form = cgi.FieldStorage()
# 获取文件名
fileList = form['filename']
for fileitem in fileList:
    if fileitem.filename:
     print(fileitem.filename+"</br>")
     fn = os.path.basename(fileitem.filename)
     file=open("F://"+fn,"wb")
     while True:
      """
      一块一块地读，保证大文件也能顺利读取
      """   
      data=fileitem.file.read(1024)    
      file.write(data)
      file.flush()
      if not data:
         break    
     file.close()
     message = '文件"' + fn + '"上传成功</br>'
    else:
       message = '没有文件需要上传'
    print("<html><body>")
    print(message)
    print("</body></html>")
