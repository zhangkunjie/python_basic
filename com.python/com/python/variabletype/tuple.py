#coding=utf-8
"""
元组是不允许更新的，只能读取
"""
#Tuple（元组）
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print (tuple) # 输出完整元组
print (tuple[0]) # 输出元组的第一个元素
print (tuple[1:3]) # 输出第二个至第三个的元素
print (tuple[2:]) # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2) # 输出元组两次
print (tuple + tinytuple) # 打印组合的元组
print (tuple.count(2.23))#输出包含元素的个数
"""元组不允许更新"""
#tuple[1]=1000;
print(tuple[1])
"""但是元组可以合并"""
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# 以下修改元组元素操作是非法的。
# tup1[0] = 100;

# 创建一个新的元组
tup3 = tup1 + tup2;
print (tup3);