'''
将对象转换成json
'''
from collections import namedtuple
import json

import demjson


class Student():
    def __init__(self, id,name,sex,age):
        self.id=id
        self.name=name
        self.sex=sex
        self.age=age
    def to_JSON(self):
        return json.dumps(self.__dict__,indent=2) 
"""
对象转换成json
"""    
s=Student(1,'张三',1,20)
print(s.to_JSON()) 
"""
json转换成对象
"""
s = '{ "id":1,"name":"John Smith","sex":1,"age":25 }'
x = json.loads(s, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
print (x.id,x.age)
"""
* 用来传递任意个无名字参数，这些参数会一个Tuple的形式访问。
**用来处理传递任意个有名字的参数，这些参数用dict来访问。
"""
j = json.loads(s)
print(j)
u = Student(**j)
print(u.name,u.age)