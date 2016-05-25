"""
dumps:对数据进行编码:元组会被转换成列表
"""
import json
from json.decoder import JSONArray
org_data= [[3,2,1],10,7,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
dumps_data = json.dumps(org_data)
print (repr(org_data))
print (dumps_data[2])
"""
loads:对数据进行解码:解码之前，数据就是一个字符串，解码之后变成了json对象
"""
loads_data=json.loads(dumps_data)
print(loads_data[2])
dict=loads_data[4]
print(dict)
keyList=loads_data[4].keys()
for k in keyList:
    print(k)
valueList=loads_data[4].values()
for v in valueList:
    print(v)
for i in  dict.items():
    print(str(i[0])+str(i[1]))
for n in dict:
    print(str(n)+str(dict[n]))

