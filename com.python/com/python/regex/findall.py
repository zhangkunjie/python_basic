# coding=utf-8
import re
"""
可以使用re.split来分割字符串，如：re.split(r'\s+', text)；将字符串按空格分割成一个单词列表。
"""
#全部替换
s="Cat is smarter Cat smarter than dog"
news1= re.split("smarter", s, 1)
print(news1)
news2= re.split("smarter", s, 2)
print(news2)