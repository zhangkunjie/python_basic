#coding=utf-8
"""
python的字串列表有2种取值顺序:
    从左到右索引默认0开始的，最大范围是字符串长度少1
    从右到左索引默认-1开始的，最大范围是字符串开头
"""
str = 'Hello World!'
print (str) # 输出完整字符串
print (str[0]) # 输出字符串中的第一个字符
print (str[2:5]) # 输出字符串中第三个至第五个之间的字符串
print (str[2:]) # 输出从第三个字符开始的字符串
print (str * 2) # 输出字符串两次
print (str + "TEST") # 输出连接的字符串 