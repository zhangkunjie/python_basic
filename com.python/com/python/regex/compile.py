# coding=utf-8
import re
"""
re.findall可以获取字符串中所有匹配的字符串。如：re.findall(r'\w*oo\w*', text)；获取字符串中，包含'oo'的所有单词。
"""
text = '<a href="http://movie.douban.com/subject/24397586/?from=tag_all" class="title/1234456/" target="_blank">小羊肖恩 Shaun the Sheep Movie</a>'
regex = re.compile(r'/\d+/')
print (regex.findall(text))   #查找所有包含'oo'的单词
print (regex.sub(lambda m: '[' + m.group(0) + ']', text)) #将字符串中含有'oo'的单词用[]括起来。