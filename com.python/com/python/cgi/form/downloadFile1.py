#!D:\Program Files\Python\python.exe
# coding=utf-8
# HTTP Header
import io
import os
import sys


print ("Content-Type:application/octet-stream; name=\"abc.pdf\"")
print ("Content-Disposition: application/octet-stream; filename=\"abc.pdf\"\r\n\n")
sys.stdout.flush()
with io.open(sys.stdout.fileno(),"wb") as fout:
    with open("D://abc.pdf","rb") as fin:
        while True:
            data = fin.read(4096)
            fout.write(data)
            if not data:
                break
