# coding=utf-8
"""
==    等于 - 比较对象是否相等    (a == b) 返回 False。
!=    不等于 - 比较两个对象是否不相等    (a != b) 返回 true.
>    大于 - 返回x是否大于y    (a > b) 返回 False。
<    小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。    (a < b) 返回 true。
>=    大于等于 - 返回x是否大于等于y。    (a >= b) 返回 False。
<=    小于等于 - 返回x是否小于等于y。    (a <= b) 返回 true。 
"""
a = 21
b = 10
c = 0

if ( a == b ):
   print ("Line 1 - a is equal to b")
else:
   print ("Line 1 - a is not equal to b")

if ( a != b ):
   print ("Line 2 - a is not equal to b")
else:
   print ("Line 2 - a is equal to b")
if ( a < b ):
   print ("Line 4 - a is less than b" )
else:
   print ("Line 4 - a is not less than b")

if ( a > b ):
   print ("Line 5 - a is greater than b")
else:
   print ("Line 5 - a is not greater than b")

a = 5;
b = 20;
if ( a <= b ):
   print ("Line 6 - a is either less than or equal to  b")
else:
   print ("Line 6 - a is neither less than nor equal to  b")

if ( b >= a ):
   print ("Line 7 - b is either greater than  or equal to b")
else:
   print ("Line 7 - b is neither greater than  nor equal to b")