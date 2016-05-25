# coding=utf-8
"""
continue
"""
i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print (i)         # 输出双数2、4、6、8、10