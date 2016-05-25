#coding=utf-8
#List（列表） 是 Python 中使用最频繁的数据类型。
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list) # 输出完整列表
print (list[0]) # 输出列表的第一个元素
print (list[1:3]) # 输出第二个至第三个的元素
print (list[2:] )# 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2) # 输出列表两次
print (list + tinylist) # 打印组合的列表

"""列表是允许更新的，元组不行"""
list[1]=1000;
print(list[1])
"""分割list"""
list = ['a','b','c']
print("#".join(list))