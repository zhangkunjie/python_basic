#coding=utf-8
"""
字典是另一种可变容器模型，且可存储任意类型对象，如字符串、数字、元组等其他容器模型
"""
#Dictionary字典
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print (dict['Beth'])
#修改字典
dict["Beth"]=12345
print (dict['Beth'])
#得到字典长度
print(len(dict))
#得到字段所以keys
print(dict.keys())
#得到字段所以values
print(dict.values())
#删除字典元素
del dict["Beth"]
print(dict)
#清空字典
dict.clear()
print(dict)
#删除字典
del dict
#print(dict)
"""键必须不可变，所以可以用数，字符串或元组充当，所以用列表就不行"""
#dict = {['Name']: 'Zara', 'Age': 7};
#print ("dict['Name']: ", dict['Name']);
"""
字典内置方法
1、cmp(dict1, dict2)：比较两个字典元素。
2、len(dict)：计算字典元素个数，即键的总数。
3、str(dict)：输出字典可打印的字符串表示。
4、type(variable)：返回输入的变量类型，如果变量是字典就返回字典类型。
Python字典包含了以下内置方法：
1、radiansdict.clear()：删除字典内所有元素
2、radiansdict.copy()：返回一个字典的浅复制
3、radiansdict.fromkeys()：创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4、radiansdict.get(key, default=None)：返回指定键的值，如果值不在字典中返回default值
5、radiansdict.has_key(key)：如果键在字典dict里返回true，否则返回false
6、radiansdict.items()：以列表返回可遍历的(键, 值) 元组数组
7、radiansdict.keys()：以列表返回一个字典所有的键
8、radiansdict.setdefault(key, default=None)：和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
9、radiansdict.update(dict2)：把字典dict2的键/值对更新到dict里
10、radiansdict.values()：以列表返回字典中的所有值
"""


