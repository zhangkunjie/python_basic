# coding=utf-8
"""
+    加 - 两个对象相加    a + b 输出结果 30
-    减 - 得到负数或是一个数减去另一个数    a - b 输出结果 -10
*    乘 - 两个数相乘或是返回一个被重复若干次的字符串    a * b 输出结果 200
/    除 - x除以y    b / a 输出结果 2
%    取模 - 返回除法的余数    b % a 输出结果 0
**    幂 - 返回x的y次幂    a**b 为10的20次方， 输出结果 100000000000000000000
//    取整除 - 返回商的整数部分    9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
"""
a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

c = a - b
print ("Line 2 - Value of c is ", c)

c = a * b
print ("Line 3 - Value of c is ", c) 

c = a / b
print ("Line 4 - Value of c is ", c)

c = a % b
print ("Line 5 - Value of c is ", c)

a = 2
b = 3
c = a ** b 
print ("Line 6 - Value of c is ", c)

a = 10
b = 3
c = a // b 
print ("Line 7 - Value of c is ", c)
