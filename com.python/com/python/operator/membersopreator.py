# coding=utf-8
"""
in    如果在指定的序列中找到值返回True，否则返回False。     x 在 y序列中 , 如果x在y序列中返回True。
not in    如果在指定的序列中没有找到值返回True，否则返回False。     x 不在 y序列中 , 如果x不在y序列中返回True。
"""
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print ("Line 1 - a is available in the given list")
else:
   print ("Line 1 - a is not available in the given list")

if ( b not in list ):
   print ("Line 2 - b is not available in the given list")
else:
   print ("Line 2 - b is available in the given list")

a = 2
if ( a in list ):
   print ("Line 3 - a is available in the given list")
else:
   print ("Line 3 - a is not available in the given list")