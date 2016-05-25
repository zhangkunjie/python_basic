# coding=utf-8
import re
"""
正则表达式主要有一下几个方法：
match search sub split findall complie
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
而re.search匹配整个字符串，直到找到一个匹配。
re.match 尝试从字符串的开始匹配一个模式。
函数语法：
re.match(pattern, string, flags=0)
函数参数说明：
参数    描述
pattern    匹配的正则表达式
string    要匹配的字符串。
flags    标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
匹配成功re.match方法返回一个匹配的对象，否则返回None。
我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
匹配对象方法    描述
group(num=0)    匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()    返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
"""
s="Cat is smarter Cat than dog"
matchReg1 = re.match("Cat", s, re.M|re.I)
if matchReg1:
    print("s满足matchReg1匹配")
    print(matchReg1.group(0))
else:
    print("s不满足matchReg1匹配") 
matchReg2 = re.match("dog", s, re.M|re.I)
if matchReg2:
    print("s满足matchReg2匹配")
    print(matchReg1.group(0))
else:
    print("s不满足matchReg2匹配") 
s1='日本/ 喜剧 / 动画 /奇幻 / 2015 / 小林義地方2/张磊 |2012| 吴文伦/' 
des=str(s1).strip().replace(" ", "") 
print(des)  
year=re.compile(r"/(\d+[0-9])/",re.I)
print(year.findall(des)[0]) 

