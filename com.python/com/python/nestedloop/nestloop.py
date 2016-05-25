# coding=utf-8
"""
for嵌套循环:二维数组
"""
from lib2to3.pgen2.token import STRING
from lib2to3.fixer_util import String


a=[1,2,3]
b=[4,5,6]
for i in a:
    for j in b:
        print([i,j])
    
"""
while嵌套：求100以内的质数
"""
m=2
while(m<100):
   n=2
   while(n<=(m/n)):
     if not(m%n):break
     n=n+1
   if(n>m/n):print(m,"是质数") 
   m=m+1
print("Good bye!")
