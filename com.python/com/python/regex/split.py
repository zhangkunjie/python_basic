# coding=utf-8
import re
"""
re.findall可以获取字符串中所有匹配的字符串。如：re.findall(r'\w*oo\w*', text)；获取字符串中，包含'oo'的所有单词。
"""
text = "JGood is a handsome boy, he is cool, clever, and so on..."
regex = re.compile(r'\w*oo\w*')
print (regex.findall(text))   #查找所有包含'oo'的单词
print (regex.sub(lambda m: '[' + m.group(0) + ']', text)) #将字符串中含有'oo'的单词用[]括起来。