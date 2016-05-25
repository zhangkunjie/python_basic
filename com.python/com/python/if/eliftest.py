# coding=utf-8
"""
if 判断条件1:
    执行语句1……
elif 判断条件2:
    执行语句2……
elif 判断条件3:
    执行语句3……
else:
    执行语句4……
注意：python没有switch语句，所以多条件分支只能使用elif
"""
num = 5     
if num == 3:            # 判断num的值
    print ('boss')        
elif num == 2:
    print ('user')
elif num == 1:
    print ('worker')
elif num < 0:           # 值小于零时输出
    print ('error')
else:
    print ('roadman')    # 条件均不成立时输出
