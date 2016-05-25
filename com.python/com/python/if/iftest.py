# coding=utf-8
"""
if 判断条件：
    执行语句……
else：
    执行语句……
注意：if 代码块没有大括号，使用行缩进的方式来代表代码块
"""
flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True              # 条件成立时设置标志为真
    print ('welcome boss')    # 并输出欢迎信息
else:
    print (name)              # 条件不成立时输出变量名称