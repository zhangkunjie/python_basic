from com.python.classes.Parent import Parent
class Child(Parent): # 定义子类
   def __init__(self):
      print ("调用子类构造方法")

   def childMethod(self):
      print ('调用子类方法 child method')
   def run(self):
       print ('子类重写父类方法Run')   