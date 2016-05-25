# coding=utf-8
import re
"""
Python 的re模块提供了re.sub用于替换字符串中的匹配项。
语法：
re.sub(pattern, repl, string, max=0)
返回的字符串是在字符串中用 RE 最左边不重复的匹配来替换。如果模式没有发现，字符将被没有改变地返回。
可选参数 count 是模式匹配后替换的最大次数；count 必须是非负整数。缺省值是 0 表示替换所有的匹配。
"""
#全部替换
s="Cat is smarter Cat than dog"
news1= re.sub("Cat", "Cats", s)
print(news1)
#只替换一个
news2= re.sub("Cat", "Cats", s,1)
print(news2)