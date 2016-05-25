#coding=utf-8
from com.python.classes.Child import Child
from com.python.classes.Parent import Parent
p=Parent()
c=Child()
c.childMethod()
c.parentMethod()
c.setAttr(200) 
print("AAAAAa",c.getAttr())
print(issubclass(Child,Parent))
print(isinstance(c, Child))
print(isinstance(c, Parent))
print(c.run())
p.setAge(100)
print(p.getAge())