#coding=utf-8
from com.python.classes.Employee import Employee
emp1=Employee("张三",23,3000)
emp2=Employee("李四",25,4000)
emp3=Employee("赵武",27,5000)
print("员工总数是：%d"%Employee.empCount)
print("张三年龄是：%d"%emp1.age)
emp1.age=25
print("属性改变后张三年龄是：%d"%getattr(emp1, 'age'))
#del emp1.age  
print("删除age属性后张三年龄是：%d"%getattr(emp1, 'age'))#报错，没有age属性
print(hasattr(emp1, 'age'))    # 如果存在 'age' 属性返回 True。
print(getattr(emp1, 'age') )   # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
print(getattr(emp1, 'age') )   # 返回 'age' 属性的值
delattr(emp1, 'age')    # 删除属性 'age'
#print ("Employee.__name__:", Employee.__name__) 
#print ("Employee.__module__:", Employee.__module__) 
#print ("Employee.__bases__:", Employee.__bases__) 
#print ("Employee.__dict__:", Employee.__dict__) 
