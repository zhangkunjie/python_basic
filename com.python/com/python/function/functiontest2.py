# coding=utf-8
"""
缺省参数
"""
def printinfo1( name, age = 35 ):
   "打印任何传入的字符串"
   print ("Name: ", name)
   print ("Age ", age)
   return;
printinfo1("张三")
printinfo1("李四",24)
"""
加了星号（*）的变量名会存放所有未命名的变量参数。选择不多传参数也可。如下实例：
"""
def printinfo2( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;printinfo2( 10 );
printinfo2( 70, 60, 50 );