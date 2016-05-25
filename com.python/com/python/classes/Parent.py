#coding=utf-8
class Parent:
    __age=0 #私有变量以两个下划线开始，访问方法参数第一个必须是self
    parentAttr = 100
    def __init__(self):
       print ("调用父类构造函数")
    def parentMethod(self):
       print ('调用父类方法')
    def run(self):
       print ('调用父类方法Run')   
    def setAttr(self, attr):
       Parent.parentAttr = attr
    def getAttr(self):
       print ("父类属性 :", Parent.parentAttr)
    def setAge(self,age):
        self.__age=age
    def getAge(self):
       return self.__age   
