# coding=utf-8
import re
"""
re.search 会在字符串内查找模式匹配，直到找到第一个匹配。
函数语法：
re.search(pattern, string, flags=0)
函数参数说明：
参数    描述
pattern    匹配的正则表达式
string    要匹配的字符串。
flags    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
匹配成功re.search方法返回一个匹配的对象，否则返回None。
我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
匹配对象方法    描述
group(num=0)    匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()    返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
"""
s="Cat is smarter Cat than dog"
searchReg1 = re.search("Cat", s, re.M|re.I)
if  searchReg1:
    print("s满足searchReg1匹配")
    print(searchReg1.group())
else:
    print("s不满足matchReg1匹配") 
searchReg2 = re.search("dog", s, re.M|re.I)
if  searchReg2:
    print("s满足searchReg2匹配")
    print(searchReg2.group())
else:
    print("s不满足searchReg1匹配") 