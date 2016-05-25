#coding=utf-8

class Employee:
    empCount=0

    def __init__(self, name,age,salary):
        self.name=name
        self.salary=salary
        self.age=age
        Employee.empCount+=1
    def displayCount(self):
        print("员工总是是："+self.empCount)    
    def displayEmployee(self):
        print("姓名：",self.name,"工资：",self.salary) 
         
        