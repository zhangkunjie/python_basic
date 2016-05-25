# coding=utf-8
"""
函数定义原则：
    函数代码块以def关键词开头，后接函数标识符名称和圆括号()。
    任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
 Return[expression]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""
def print_list(list):
    for i in list:
     print(i)
print_list([1,2,3,4,5])     
