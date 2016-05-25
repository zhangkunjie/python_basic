# coding=utf-8
"""
运算符    描述    实例
=    简单的赋值运算符    c = a + b 将 a + b 的运算结果赋值为 c
+=    加法赋值运算符    c += a 等效于 c = c + a
-=    减法赋值运算符    c -= a 等效于 c = c - a
*=    乘法赋值运算符    c *= a 等效于 c = c * a
/=    除法赋值运算符    c /= a 等效于 c = c / a
%=    取模赋值运算符    c %= a 等效于 c = c % a
**=    幂赋值运算符    c **= a 等效于 c = c ** a
//=    取整除赋值运算符    c //= a 等效于 c = c // a
"""
a = 21
b = 10
c = 0

c = a + b
print ("Line 1 - Value of c is ", c)

c += a
print ("Line 2 - Value of c is ", c)

c *= a
print ("Line 3 - Value of c is ", c) 

c /= a 
print ("Line 4 - Value of c is ", c) 

c  = 2
c %= a
print ("Line 5 - Value of c is ", c)

c **= a
print ("Line 6 - Value of c is ", c)

c //= a
print ("Line 7 - Value of c is ", c)